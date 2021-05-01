from view import View
import firebase_admin
from firebase_admin import db
import json
from newsapi import NewsApiClient
from pandas import json_normalize
import tkinter as tk
import webbrowser
from bs4 import BeautifulSoup
import requests
import copy
import random  # required for choosing a random response
import pickle  # Python object serialization
import numpy as np
import nltk  # natural language tool kit
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import tensorflow as tf


class Model:
    def __init__(self):
        print("Model Initialised")

    def connect_to_database(self):
        self.ref = db.reference("/")  # setting reference to the root of the table
        self.target = {}
        cred_obj = firebase_admin.credentials.Certificate(
            r"../../Assets/files/ctextinct-firebase-adminsdk-xnpem-e13f73b9d2.json")
        default_app = firebase_admin.initialize_app(cred_obj, {
            'databaseURL': "https://ctextinct-default-rtdb.europe-west1.firebasedatabase.app/"
        })

    def write_to_database(self):
        self.ref.set({
            "News":
                {
                    "Article": -1
                }
        })
        self.ref = db.reference("/News/Article")

        # with statement automatically closes the file handler
        with open(r"../../Assets/files/feedback_responses.json", "r") as file_handler:
            file_contents = json.load(file_handler)  # convert json to python dictionary
        print(file_contents)
        for key, value in file_contents.items():
            self.ref.push().set(value)

    def update_database(self):
        self.ref = db.reference("/Books/Best_Sellers/")
        self.target = self.ref.get()
        print(self.target)
        for key, value in self.target.items():
            if value["Author"] == "J.R.R. Tolkien":
                value["Price"] = 90
                self.ref.child(key).update({"Price": 80})

    def retrieve_data_from_database(self):
        self.ref = db.reference("/Books/Best_Sellers/")
        print(self.ref.order_by_child("Price").get())
        self.ref.order_by_child("Price").limit_to_last(1).get()
        self.ref.order_by_child("Price").limit_to_first(1).get()
        self.ref.order_by_child("Price").equal_to(80).get()

    def delete_data_from_database(self):
        self.ref = db.reference("/Books/Best_Sellers")
        for key, value in self.target.items():
            if value["Author"] == "J.R.R. Tolkien":
                self.ref.child(key).set({})

    def visit_news(v):
        webbrowser.open_new_tab(v)

    def connect_to_News_API(self):
        self.cache = None
        self.news_buttons = []
        self.counter = 0
        self.newsapi = NewsApiClient(
            api_key='1fa3d77b9ae7460c833ef91fe447eca4')  # generated my own api key by registering
        country = "gb"
        category = "technology"
        self.top_titles = self.newsapi.get_top_headlines(category=category,
                                                         language='en', country=country)
        self.top_titles = json_normalize(self.top_titles['articles'])  # top_headlines organised in json format
        print(self.top_titles)
        new_df = self.top_titles[["title", "url"]]  # grabbing each top titles' title and urls
        self.dic = new_df.set_index('title')['url'].to_dict()
        # creating dictionary with the value being the url and the title as the key

    def switch(self):
        if self.counter == 1:
            for i in self.news_buttons:
                self.news_buttons.remove(self.news_buttons[i])
            self.counter = 0
        if self.counter == 0:
            self.counter = 1
            self.get_latest_news()

    def get_latest_news(self):
        if not self.cache:
            self.cache = self.dic
        for k, v in self.cache.items():
            temp = tk.Button(self, text=k, command=lambda: visit_news(v))
            temp.pack(pady=10, padx=10)
            self.news_buttons.append(temp)

    # "https://cybersecurityforum.com/cybersecurity-faq/"
    def cyber_security_forum_parser(self):
        self.url = url
        self.filename = self.url.split("/")[2].split(".")[
                            0] + ".json"  # will return file name cybersecurityforum.json
        self.forum_question_class_name = "faq-question"
        self.forum_answer_class_name = "faq-answer"

        self.fake_browser = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 '
                                           'Firefox/77.0'}
        self.response = requests.get(self.url, headers=self.fake_browser)  # get all the text from specified url

        self.parser = BeautifulSoup(self.response.content, features="html.parser")
        # save content of forum into variable parser aby using the html parser in BeautifulSoup()

        self.questions = [q.text.strip() for q in
                          self.parser.find_all("div", class_=self.forum_question_class_name)]
        # a single trailing underscore as seen above is used by convention to avoid conflicts with Python keywords.
        self.answers = [q.text.strip() for q in
                        self.parser.find_all("div", class_=self.forum_answer_class_name)]
        # all questions and answers from each div is collected as a list
        self.dataset_dict = dict(tag="#tag_placehodler", patterns=[], responses=[])
        # I will need to manually edit the resulting file with reasonable tags for each question
        self.intents = []  # list for dataset_dict

        # using zip to join the question and answer lists together
        for q, a in zip(self.questions, self.answers):
            temp = copy.deepcopy(
                self.dataset_dict)  # deepcopy is a method of the module copy in python that allowed
            # me to do an independent copy of the dictionary instead of just referencing it
            temp["patterns"].append(q)  # here i am filling the empty lists with the questions
            temp["responses"].append(a)
            self.intents.append(temp)

        with open("../../Assets/files/" + self.filename, "w") as f:
            json.dump(self.intents, f, indent=4, sort_keys=False)  # indent by 4 spaces and do not sort the keys

    def training_model(self):
        physical_devices = tf.config.list_physical_devices('CPU')
        # tf.config.experimental.set_memory_growth(physical_devices[0], True)
        # used when training using CUDA and NVIDIA Graphics card.

        # SGD stands for Stochastic gradient descent

        lemmatizer = WordNetLemmatizer()  # calling the wordNetLemmatizer constructor
        # the lemmatizer will reduce the word to its stem. For example, work, working, worked, works is all the same
        # stem word as "work". Wordnet is an large, freely and publicly available lexical database for the
        # English language aiming to establish structured semantic relationships between words.

        intentsDictionary = json.loads(open("intents.json").read())

        # created 3 empty lists and the letters this program will ignore
        wordList = []
        tagList = []
        documentList = []  # this list will be used for the linked tokenized words and tags
        ignoredCharList = ["?", "!", ",", "."]

        # I am iterating over the intents
        for intent in intentsDictionary["intents"]:
            # for each of the patterns, the below will tokenize the sentences.
            # Meaning the sentences will split into words.
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
        # character stream. The idea is that this character stream contains all the information necessary to
        # reconstruct the object in another python script.
        pickle.dump(wordList, open("../Assets/Files/wordList.pk1", "wb"))  # write binary
        pickle.dump(tagList, open("../Assets/Files/tagList.pk1", "wb"))

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
            training.append(
                [bag, outputRow])  # example: bag(10100010101000000000100001001000) outputRow(000010000) how many
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
        model.save("../Assets/Files/chatbot.h5", hist)
        print("Done")

    def load_files(self):
        lemmatizer = WordNetLemmatizer()
        intentsDictionary = json.loads(open("intents.json").read())

        wordList = pickle.load(open("wordList.pk1", "rb"))  # read binary
        tagList = pickle.load(open("tagList.pk1", "rb"))
        model = load_model("chatbot.h5")

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
    def predict_tag(self, sentence):
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
    def get_response(self, intents_list, intents_json):
        tag = intents_list[0]["intent"]
        list_of_intents = intents_json["intents"]
        for i in list_of_intents:
            if i["tag"] == tag:
                result_response = random.choice(i["responses"])
                break
        return result_response

    def next_question(self, response):
        self.entry.delete(0, END)
        self.responseL.configure(text=response)

    def ask_question(self, user_question):
        if user_question == "":
            user_question = "Hi"
        ints = self.predict_tag(user_question)
        response = get_response(ints, intents_dictionary)
        return response
