from bs4 import BeautifulSoup
import requests
import copy
import json


# "https://cybersecurityforum.com/cybersecurity-faq/"
class CyberSecurityForumParser:
    def __init__(self, url):
        self.url = url
        self.filename = self.url.split("/")[2].split(".")[0] + ".json"  # will return file name cybersecurityforum.json
        self.forum_question_class_name = "faq-question"
        self.forum_answer_class_name = "faq-answer"

        self.fake_browser = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 '
                                           'Firefox/77.0'}
        self.response = requests.get(self.url, headers=self.fake_browser)  # get all the text from specified url

        self.parser = BeautifulSoup(self.response.content, features="html.parser")
        # save content of forum into variable parser aby using the html parser in BeautifulSoup()

        self.questions = [q.text.strip() for q in self.parser.find_all("div", class_=self.forum_question_class_name)]
        # a single trailing underscore as seen above is used by convention to avoid conflicts with Python keywords.
        self.answers = [q.text.strip() for q in self.parser.find_all("div", class_=self.forum_answer_class_name)]
        # all questions and answers from each div is collected as a list
        self.dataset_dict = dict(tag="#tag_placehodler", patterns=[], responses=[])
        # I will need to manually edit the resulting file with reasonable tags for each question
        self.intents = []  # list for dataset_dict

        # using zip to join the question and answer lists together
        for q, a in zip(self.questions, self.answers):
            temp = copy.deepcopy(self.dataset_dict)  # deepcopy is a method of the module copy in python that allowed
            # me to do an independent copy of the dictionary instead of just referencing it
            temp["patterns"].append(q)  # here i am filling the empty lists with the questions
            temp["responses"].append(a)
            self.intents.append(temp)

        with open("../../Includes/files/" + self.filename, "w") as f:
            json.dump(self.intents, f, indent=4, sort_keys=False)  # indent by 4 spaces and do not sort the keys


x = CyberSecurityForumParser("https://cybersecurityforum.com/cybersecurity-faq/")
