import random
import json
import numpy as np
import pickle

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intentsDictionary = json.loads(open("intents.json").read())

wordList = pickle.load(open("wordList.pk1", "rb"))  # read binary
tagList = pickle.load(open("tagList.pk1", "rb"))
model = load_model("chatbot.h5")


# this function tokenizes each word in the sentence and lemmatizes it.
def cleanUpSentence(sentence):
    sentenceWords = nltk.word_tokenize(sentence)
    sentenceWords = [lemmatizer.lemmatize(eachWord) for eachWord in sentenceWords]
    return sentenceWords


# convert a sentence into Bag of Words. A list of 0s or 1s to indicate if a word is there or not.
def bagOfWords(sentence):
    sentenceWords = cleanUpSentence(sentence)
    bag = [0] * len(wordList)
    for x in sentenceWords:
        for i, thisWord in enumerate(wordList):
            if thisWord == x:
                bag[i] = 1
    return np.array(bag)


# for predicting the tag based on the sentence inputted
def predictTag(sentence):
    bagOfw = bagOfWords(sentence)  # this will be inputted into the neural network
    result = model.predict(np.array([bagOfw]))[0]  # 0 added to match the format
    ERROR_THRESHOLD = 0.25
    percentageRes = [[i, r] for i, r in enumerate(result) if r > ERROR_THRESHOLD]

    percentageRes.sort(key=lambda x: x[1], reverse=True)
    returnList = []
    for r in percentageRes:
        returnList.append({"intent": tagList[r[0]], "probability": str(r[1])})
    return returnList


# for giving a response
def getResponse(intentsList, intentsJson):
    tag = intentsList[0]["intent"]
    listOfIntents = intentsJson["intents"]
    for i in listOfIntents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result


print("Janine just joined the chat! What would you like to ask her?")

while True:
    message = input("")
    ints = predictTag(message)
    response = getResponse(ints, intentsDictionary)
    print(response)
