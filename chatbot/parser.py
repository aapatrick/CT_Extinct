from bs4 import BeautifulSoup
import requests
import copy
import json


url = "https://cybersecurityforum.com/cybersecurity-faq/"
filename = url.split("/")[2] + ".json"
questions_class_name = "faq-question"
answers_class_name = "faq-answer"



faking_browser = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
response = requests.get(url, headers = faking_browser)

parser = BeautifulSoup(response.content)

questions = [q.text.strip() for q in parser.find_all("div", class_ = questions_class_name)]
answers = [q.text.strip() for q in parser.find_all("div", class_ = answers_class_name)]
template_dict = dict(tag = "#tag_placehodler", patterns = [], responses = [])


intents = []

for q, a in zip(questions, answers):
    temp = copy.deepcopy(template_dict)
    temp["patterns"].append(q)
    temp["responses"].append(a)
    intents.append(temp)

    
with open(filename, "w") as f:
    json.dump(intents, f, indent=4, sort_keys=True)   
    