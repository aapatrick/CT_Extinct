import random
import numpy as np
import pickle  # for sterilization
import nltk
import json
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model


def get_response(intents_list, intents_json):
    result_response = ""
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result_response = random.choice(i["responses"])
            break
    return result_response


class ChatbotHandler:
    def __init__(self, intents_dictionary):
        self.intents_dictionary = json.loads(open(intents_dictionary).read())
        # read json as text and pass it to load function
        self.lemmatizer = WordNetLemmatizer()
        print("test= error intentsJson")
        self.wordList = pickle.load(open("../../Assets/files/wordList.pk1", "rb"))  # read binary
        self.tagList = pickle.load(open("../../Assets/files/tagList.pk1", "rb"))
        self.model = load_model("../../Assets/files/chatbot.h5")

        # this function tokenizes each word in the sentence and lemmatizes it.

    def cleanup_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(eachWord) for eachWord in sentence_words]
        return sentence_words

    # convert a sentence into Bag of Words. A list of 0s or 1s to indicate if a word is there or not.
    def bag_of_words(self, sentence):
        sentence_words = self.cleanup_sentence(sentence)
        bag = [0] * len(self.wordList)
        for x in sentence_words:
            for i, thisWord in enumerate(self.wordList):
                if thisWord == x:
                    bag[i] = 1
        return np.array(bag)

    # for predicting the tag based on the sentence inputted
    def predict_tag(self, sentence):
        print("Test: just before")
        bag_of_w = self.bag_of_words(sentence)  # this will be inputted into the neural network
        result_tag = self.model.predict(np.array([bag_of_w]))[0]  # 0 added to match the format
        print("Test: I MADE IT")
        ERROR_THRESHOLD = 0.25
        percentage_res = [[i, r] for i, r in enumerate(result_tag) if r > ERROR_THRESHOLD]

        percentage_res.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in percentage_res:
            return_list.append({"intent": self.tagList[r[0]], "probability": str(r[1])})
        return return_list

    print("finished")

# test = ChatbotHandler("../../Assets/files/intents.json")
# test.predict_tag("Hi")
