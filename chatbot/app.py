import tkinter as tk
from tkinter import ttk

import webbrowser
from PIL import ImageTk, Image
from chat import *
from newsApi import *
from newsapi import NewsApiClient
from pandas import json_normalize

root = tk.Tk()  # calls the ttk constructor method to create a new top-level widget, the main window, and assign it
# the variable named root


class Chatbot:

    def __init__(self, master):
        self.entry = ttk.Entry(master, fg="white", bg="#073529", width=50, borderwidth=10)
        self.responseL = ttk.Label(master, text="Janine just joined the chat! What would you like to ask her?",
                                   fg="white", bg="#073529", width=50, pady=25, wraplength=300, borderwidth=10,
                                   relief="flat")
        self.securityQ_b = ttk.Button(master, text="Ask Security Questions", fg="#073529", bg="#D2D0D5", padx=50,
                                      pady=25, borderwidth=10, relief="solid")
        master.bind('<Return>', self.ask_question)
        self.entry.insert(0, "Type your question here")

        self.entry.grid(row=20, column=1, columnspan=2, padx=50, pady=50)
        self.responseL.grid(row=30, column=1, columnspan=2)
        self.securityQ_b.grid(row=50, column=0)

    @staticmethod
    def next_question(response):
        Chatbot.entry.delete(0, ttk.END)
        Chatbot.responseL.configure(text=response)

    @staticmethod
    def ask_question():
        user_q = Chatbot.entry.get()
        ints = predict_tag(user_q)
        response = get_response(ints, intentsDictionary)
        Chatbot.next_question()


class Feedback:

    def __init__(self, master):
        self.feedback_b = ttk.Button(master, text="Feedback/Complaint", fg="#073529", bg="#D2D0D5", padx=50, pady=25,
                                     borderwidth=10, relief="solid")
        self.feedback_b.grid(row=50, column=3)


class Incident:

    def __init__(self, master):
        self.incident_b = ttk.Button(master, text="Security Incident", fg="#073529", bg="#D2D0D5", padx=50, pady=25,
                                     borderwidth=10, relief="solid")
        self.incident_b.grid(row=50, column=1)


class News:

    def __init__(self, master):
        self.news_buttons = []
        self.counter = 0
        self.cache = None
        self.news_b = ttk.Button(master, text="Latest News", fg="#073529", bg="#D2D0D5", padx=50, pady=25,
                                 command=self.switch, borderwidth=10, relief="solid")
        self.news_b.grid(row=50, column=2)

    # I made this method static because the headlines will not be different for every new instance of
    @staticmethod  # the class 'News' -- they will always be the same for all instances
    def top_headlines():
        newsapi = NewsApiClient(api_key='1fa3d77b9ae7460c833ef91fe447eca4')
        country = "gb"
        category = "technology"
        top_titles = newsapi.get_top_headlines(category=category,
                                               language='en', country=country)
        top_titles = json_normalize(top_titles['articles'])
        new_df = top_titles[["title", "url"]]
        dic = new_df.set_index('title')['url'].to_dict()
        return dic

    @staticmethod
    def visit_news(v):
        webbrowser.open_new_tab(v)

    def switch(self):
        if Chatbot.counter == 1:
            for i in self.news_buttons:
                Chatbot.news_buttons.remove(Chatbot.news_buttons[i])
            Chatbot.counter = 0
        if Chatbot.counter == 0:
            Chatbot.counter = 1
            Chatbot.get_latest_news()

    def get_latest_news(self):
        cache = ""
        if not cache:
            cache = self.top_headlines()
        for k, v in cache.items():
            temp = ttk.Button(self.master, text=k, command=lambda: self.visit_news(v))
            temp.grid(column=1, columnspan=2)
            self.news_buttons.append(temp)


def main():
    root.title("CT Extinct")
    root.iconbitmap("../assets/images/individualLogo.ico")
    root.space_l = ttk.Label(root, padx=50, pady=100)
    root.space_l2 = ttk.Label(root, padx=50, pady=50)
    root.space_l.grid(row=50)
    root.space_l2.grid(row=0)
    root.logo_pic = ImageTk.PhotoImage(Image.open("../assets/images/ardonagh.png")).subsample(10, 10)
    root.img_label = ttk.Label(root, image=logo_pic)
    root.img_label.grid(row=5, column=1, columnspan=2)
    root.logo_pic.place(x=0, y=0)
    root.after(2000, root.logo_pic.destroy)
    chatbot = Chatbot(root)
    feedback = Feedback(root)
    incident = Incident(root)
    news = News(root)

    root.mainloop()


if __name__ == "__main__":
    main()
else:
    print('This module cannot be imported or used by another module. Please run code from app.py file')

# INFO
# button['text'] = 'Press Me'
# button.config() --returns all properties
# button.invoke()
# button.state(['!disabled'])   --- active and focus are other properties..
# button.instate(['disabled']) --- is my button disabled true or false
# image.subsample
# str(button) --- returns .32452345 but str(root) returns only .
# wraplength=150
# justify = CENTER
# font = ('Courier', 18, 'bold')
# if label has image and text you can use proprty 'compound = centre'
