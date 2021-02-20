import random  # required for choosing a random response
import json
import pickle  # for serialization
import numpy as no  # for np

import nltk  # natural language tool kit
from nltk.stem import WordNetLemmatizer
# the lemmatizer will reduce the word to its stem. For example, work, working, worked, works is all the same stem
# word as "work"
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
# SGD stands for Stochastic gradient descent

lemmatizer = WordNetLemmatizer

intentsDictionary = json.loads(open("intents.json").read())

# created 3 empty lists and the letters this program will ignore
words = []
classes = []
documents = []  # the belongings
ignore_letters = ["?", "!", ",", "."]

# I am iterating over the intents
for intent in intentsDictionary["intents"]:
    # for each of the patterns, the below will tokenize the sentences. Meaning the sentences will split into words.
    for pattern in intent["patterns"]:
        listOfWords = nltk.word_tokenize(pattern)
        words.extend(listOfWords)
        documents.append((listOfWords, intent["tag"]))
        # for each tag discovered, if not added to the classes list yet, it becomes added.
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

print(documents)
