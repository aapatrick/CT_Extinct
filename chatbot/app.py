#  I did not import everything "*"
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
from PIL import ImageTk, Image
from chat import get_response, predict_tag, intentsDictionary
from newsapi import NewsApiClient
from pandas import json_normalize


load_screen = tk.Tk()
root = tk.Tk()  # calls the ttk constructor method to create a new top-level widget, the main window, and assign it
# the variable named root


class Chatbot:
    def __init__(self, master):
        self.master = master
        self.entry = ttk.Entry(master)
        self.responseL = ttk.Label(master, text="Janine just joined the chat! What would you like to ask her?")
        self.securityQ_b = ttk.Button(master, text="Ask Security Questions")
        self.master.bind('<Return>', self.ask_question())
        self.entry.grid(row=20, column=1, columnspan=2)
        self.responseL.grid(row=30, column=1, columnspan=2)
        self.securityQ_b.grid(row=50, column=0)

    def next_question(self, response):
        self.entry.delete(0, "end")
        self.responseL.configure(text=response)

    def ask_question(self):
        user_q = self.entry.get()
        ints = predict_tag(user_q)
        response = get_response(ints, intentsDictionary)
        self.next_question(response)


class Feedback:

    def __init__(self, master):
        self.feedback_b = ttk.Button(master, text="Feedback/Complaint")
        self.feedback_b.grid(row=50, column=3)


class Incident:

    def __init__(self, master):
        self.incident_b = ttk.Button(master)
        self.incident_b.grid(row=50, column=1)


class News:

    def __init__(self, master):
        self.news_buttons = []
        self.cache = None
        self.counter = 0
        self.news_b = ttk.Button(master, command=self.switch)
        self.news_b.grid(row=50, column=2)

    def top_headlines(self):
        newsapi = NewsApiClient(api_key='1fa3d77b9ae7460c833ef91fe447eca4')
        country = "gb"
        category = "technology"
        top_titles = newsapi.get_top_headlines(category=category,
                                               language='en', country=country)
        top_titles = json_normalize(top_titles['articles'])
        new_df = top_titles[["title", "url"]]
        dic = new_df.set_index('title')['url'].to_dict()
        return dic

    def visit_news(self, v):
        webbrowser.open_new_tab(v)

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
            self.cache = self.top_headlines()
        for k, v in self.cache.items():
            temp = ttk.Button(Chatbot.master, text=k, command=lambda: self.visit_news(v))
            temp.grid(column=1, columnspan=2)
            self.news_buttons.append(temp)


def main():
    load_screen.destroy()
    root.title("CT Extinct")
    root.iconbitmap("../assets/images/individualLogo.ico")
    root.geometry("500x1500")
    #chatbot = Chatbot(root)
    #feedback = Feedback(root)
    #incident = Incident(root)
    #news = News(root)




load_screen.geometry("500x1000")
# Hide Title bar
load_screen.overrideredirect(True)
splash_logo = ImageTk.PhotoImage(Image.open("../assets/images/individualLogo.ico"))
splash_label = tk.Label(load_screen, image=splash_logo)
splash_label.place(relx=0.5, rely=0.5, anchor=CENTER)
load_screen.after(5000, main())
mainloop()


#if __name__ == "__main__":
#    load_app()
#else:
#    print('This module cannot be imported or used by another module. Please run code from app.py file')


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
# if label has image and text you can use property 'compound = centre'
