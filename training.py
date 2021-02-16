import random
import json
import pickle
import numpy as no

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SFG

lemmatizer = WorldNetLemmatizer()

Intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ["?", "!", ",", "."]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend((word_list,intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

print(documents)
