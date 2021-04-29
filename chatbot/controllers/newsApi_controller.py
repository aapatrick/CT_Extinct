from newsapi import NewsApiClient
from pandas import json_normalize
import tkinter as tk
import webbrowser


def visit_news(v):
    webbrowser.open_new_tab(v)


class CyberNewsTopHeadings:
    def __init__(self):
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
