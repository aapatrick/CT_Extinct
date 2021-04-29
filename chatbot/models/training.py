import random  # required for choosing a random response
import json
import pickle  # Python object serialization
import numpy as np
import nltk  # natural language tool kit
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD


#  import tensorflow as tf


def build_neural_network_model(train_x, train_y):
    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation="softmax"))  #

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

    hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
    model.save("../../Assets/files/chatbot.h5", hist)
    print("Done")


class TrainChatbot:
    def __init__(self, file_path):
        # self.physical_devices = tf.config.list_physical_devices('GPU')
        # tf.config.experimental.set_memory_growth(self.physical_devices[0], True)
        # used when training using CUDA and NVIDIA Graphics card.
        # SGD stands for Stochastic gradient descent
        self.lemmatizer = WordNetLemmatizer()  # calling the wordNetLemmatizer constructor
        # the lemmatizer will reduce the word to its stem. E.g. work, working, worked, works is all the same stem
        # word as "work". Wordnet is an large, publicly available lexical database for the English language aiming
        # to establish structured semantic relationships between words.
        self.intents_dictionary = json.loads(open(file_path).read())
        # created 3 empty lists and the letters this program will ignore
        self.wordList = []
        self.tagList = []
        self.documentList = []  # this list will be used for the linked tokenized words and tags
        self.ignoredCharList = ["?", "!", ",", "."]
        self.tokenize_lemmatize_and_link_to_tag()

    def tokenize_lemmatize_and_link_to_tag(self):
        for intent in self.intents_dictionary["intents"]:
            # for each of the patterns, the below will tokenize the sentences splitting the sentences into words.
            for pattern in intent["patterns"]:
                listOfWords = nltk.word_tokenize(pattern)
                self.wordList.extend(listOfWords)
                self.documentList.append((listOfWords, intent["tag"]))
                # for each tag discovered, if not added to the classes list yet, it becomes added.
                if intent["tag"] not in self.tagList:
                    self.tagList.append(intent["tag"])
        print(self.documentList)  # testing purposes

        # replacing the contents of wordList with a lemmatized version excluding the "ignoredCharList"
        for eachWord in self.wordList:
            if eachWord not in self.ignoredCharList:
                self.wordList = [self.lemmatizer.lemmatize(eachWord)]
        self.eliminate_duplicate_and_serialization()

    def eliminate_duplicate_and_serialization(self):
        self.wordList = sorted(set(self.wordList))
        self.tagList = sorted(set(self.tagList))
        print(self.wordList)  # testing purposes
        print(self.tagList)  # testing purposes
        # Next, I am saving the data into files. Pickling is a way to convert a python object (list, dict, etc.) into a
        # character stream. The idea is that this character stream contains all the information necessary to reconstruct
        # the object in another python script.
        pickle.dump(self.wordList, open("../../Assets/files/wordList.pk1", "wb"))  # much faster if pickled
        pickle.dump(self.tagList, open("../../Assets/files/tagList.pk1", "wb"))  # converts to byte stream
        # also I pickled so I do not have to re-train model everytime, and just load the pickle file instead.
        self.convert_to_numerical()
        # The above organised data is not yet numerical, which is what we need for a machine learning algorithm.
        # The below code assigns 0 or 1 to each of the words depending on

    def convert_to_numerical(self):
        training_data = []
        outputEmpty = [0] * len(self.tagList)  # as many 0 as there are classes
        # turning our data into Matrices, (harder than image data (because RGB uses numbers))
        for document in self.documentList:
            bag = []  # bag of words model used here--- the inputs of 1s & 0s into the machine learning algorithm
            wordPatterns = document[0]  # each  document is a list of (pattern and related tag)
            wordPatterns = [self.lemmatizer.lemmatize(eachWord.lower()) for eachWord in wordPatterns]
            # if a word in wordlist is equal to word in wordPatterns than add 1 to bag, if not add 0.
            for eachWord in self.wordList:
                bag.append(1) if eachWord in wordPatterns else bag.append(0)

            outputRow = list(outputEmpty)  # copying outputEmpty into OutputRow.
            outputRow[self.tagList.index(document[1])] = 1  # The output row is the "Prediction" of the related tag
            training_data.append(
                [bag, outputRow])  # example: bag(10100010101000000000100001001000) outputRow(000010000) how many
            # words relate to a certain tag
        # preprocessing the data
        random.shuffle(training_data)
        training_data = np.array(training_data)  # converting to numpy array, it is faster than list, used for numerical

        train_x = list(training_data[:, 0])  # features that we wil use
        train_y = list(training_data[:, 1])  # labels that we will use to train
        build_neural_network_model(train_x, train_y)


training = TrainChatbot("../../Assets/files/intents.json")
