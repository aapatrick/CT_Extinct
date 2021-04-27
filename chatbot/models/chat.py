import random
import json
import numpy as np
import pickle
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intentsDictionary = json.loads(open("../../Includes/files/intents.json").read())

wordList = pickle.load(open("../../Includes/files/wordList.pk1", "rb"))  # read binary
tagList = pickle.load(open("../../Includes/files/tagList.pk1", "rb"))
model = load_model("../../Includes/files/chatbot.h5")


# this function tokenizes each word in the sentence and lemmatizes it.
def cleanup_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(eachWord) for eachWord in sentence_words]
    return sentence_words


# convert a sentence into Bag of Words. A list of 0s or 1s to indicate if a word is there or not.
def bag_of_words(sentence):
    sentence_words = cleanup_sentence(sentence)
    bag = [0] * len(wordList)
    for x in sentence_words:
        for i, thisWord in enumerate(wordList):
            if thisWord == x:
                bag[i] = 1
    return np.array(bag)


# for predicting the tag based on the sentence inputted
def predict_tag(sentence):
    bag_of_w = bag_of_words(sentence)  # this will be inputted into the neural network
    result_tag = model.predict(np.array([bag_of_w]))[0]  # 0 added to match the format
    ERROR_THRESHOLD = 0.25
    percentage_res = [[i, r] for i, r in enumerate(result_tag) if r > ERROR_THRESHOLD]

    percentage_res.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in percentage_res:
        return_list.append({"intent": tagList[r[0]], "probability": str(r[1])})
    return return_list


# for giving a response
def get_response(intents_list, intents_json):
    result_response = ""
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result_response = random.choice(i["responses"])
            break
    return result_response
