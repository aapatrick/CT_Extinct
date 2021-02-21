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
