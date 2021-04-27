import random  # required for choosing a random response
import json
import pickle  # Python object serialization
import numpy as np

import nltk  # natural language tool kit
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('CPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)  # used when training using CUDA and NVIDIA
# Graphics card.

# SGD stands for Stochastic gradient descent

lemmatizer = WordNetLemmatizer()  # calling the wordNetLemmatizer constructor
# the lemmatizer will reduce the word to its stem. For example, work, working, worked, works is all the same stem
# word as "work". Wordnet is an large, freely and publicly available lexical database for the English language aiming
# to establish structured semantic relationships between words.

intentsDictionary = json.loads(open("../../Includes/files/intents.json").read())

# created 3 empty lists and the letters this program will ignore
wordList = []
tagList = []
documentList = []  # this list will be used for the linked tokenized words and tags
ignoredCharList = ["?", "!", ",", "."]

# I am iterating over the intents
for intent in intentsDictionary["intents"]:
    # for each of the patterns, the below will tokenize the sentences. Meaning the sentences will split into words.
    for pattern in intent["patterns"]:
        listOfWords = nltk.word_tokenize(pattern)
        wordList.extend(listOfWords)
        documentList.append((listOfWords, intent["tag"]))
        # for each tag discovered, if not added to the classes list yet, it becomes added.
        if intent["tag"] not in tagList:
            tagList.append(intent["tag"])

print(documentList)  # testing purposes
# replacing the contents of wordList with a lemmatized version excluding the "ignore_letters"
wordList = [lemmatizer.lemmatize(eachWord) for eachWord in wordList if eachWord not in ignoredCharList]

# to eliminate the duplicates and sort the list
wordList = sorted(set(wordList))
tagList = sorted(set(tagList))
print(wordList)  # testing purposes
print(tagList)  # testing purposes
# Next, I am saving the data into files. Pickling is a way to convert a python object (list, dict, etc.) into a
# character stream. The idea is that this character stream contains all the information necessary to reconstruct the
# object in another python script.
pickle.dump(wordList, open("../../Includes/files/wordList.pk1", "wb"))  # write binary
pickle.dump(tagList, open("../../Includes/files/tagList.pk1", "wb"))

# The above organised data is not yet numerical, which is what we need for a machine learning algorithm.
# The below code assigns 0 or 1 to each of the words depending on
training = []
outputEmpty = [0] * len(tagList)  # as many 0 as there are classes
# turning our data into Matrices, (harder than image data (because RGB uses numbers))
for document in documentList:
    bag = []  # bag of words model used here--- the inputs of 1s & 0s into the machine learning algorithm
    wordPatterns = document[0]  # each document is a list of (pattern and related tag)
    wordPatterns = [lemmatizer.lemmatize(eachWord.lower()) for eachWord in wordPatterns]
    # if a word in wordlist is equal to word in wordPatterns than add 1 to bag, if not add 0.
    for eachWord in wordList:
        bag.append(1) if eachWord in wordPatterns else bag.append(0)

    outputRow = list(outputEmpty)  # copying outputEmpty into OutputRow.
    outputRow[tagList.index(document[1])] = 1  # The output row is the "Prediction" of the related tag
    training.append([bag, outputRow])  # example: bag(10100010101000000000100001001000) outputRow(000010000) how many
    # words relate to a certain tag
# preprocessing the data
random.shuffle(training)
training = np.array(training)  # converting to numpy array

trainX = list(training[:, 0])  # features that we wil use
trainY = list(training[:, 1])  # labels that we will use to train

# Start of building Neural Network model
model = Sequential()
model.add(Dense(128, input_shape=(len(trainX[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(trainY[0]), activation="softmax"))  #

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

hist = model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)
model.save("../../Includes/files/chatbot.h5", hist)
print("Done")
