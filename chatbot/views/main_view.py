import tkinter as tk
from tkinter import END

from chatbot.models.cyber_chat import ChatbotHandler, get_response
from chatbot.controllers.newsApi_controller import CyberNewsTopHeadings


class SplashScreen(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        title_sl = tk.Label(self, text="SPLASH SCREEN", font="Helvetica")
        title_sl.pack(pady=10, padx=10)
        nav_sb = tk.Button(self, text="Cyber Chat", command=lambda: controller.show_frame_type(CyberChatbot))
        nav_sb.pack(pady=10, padx=10)
        print("You are in the SPLASH SCREEN now!")


class CyberChatbot(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        chat_ci = tk.Entry(self)
        chat_ci.pack(pady=10, padx=10)
        nav_cb = tk.Button(self, text="Cyber News", command=lambda: controller.show_frame_type(CyberNews))
        nav_cb.pack(pady=10, padx=10)
        self.entry = tk.Entry(master)
        self.responseL = tk.Label(master, text="Janine just joined the chat! What would you like to ask her?")
        self.securityQ_b = tk.Button(master, text="Ask Security Questions")
        self.master.bind('<Return>', self.ask_question())
        self.entry.pack(row=20, column=1, columnspan=2)
        self.responseL.pack(pady=10, padx=10)(row=30, column=1, columnspan=2)
        self.securityQ_b.pack(pady=10, padx=10)
        print("You are in the CYBER CHAT now!")

    def next_question(self, response):
        self.entry.delete(0, END)
        self.responseL.configure(text=response)

    def ask_question(self):
        user_q = self.entry.get()
        if user_q == "":
            user_q = "Hi"
        chatbot_handler = ChatbotHandler("../Assets/files/intents.json")
        ints = chatbot_handler.predict_tag(user_q)
        response = get_response(ints, chatbot_handler.intents_dictionary)
        self.next_question(response)


class CyberNews(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        title_nl = tk.Label(self, text="Cyber News", font="Helvetica")
        title_nl.pack(pady=10, padx=10)
        nav_nb = tk.Button(self, text="Feedback", command=lambda: controller.show_frame_type(FeedbackForm))
        nav_nb.pack(pady=10, padx=10)
        self.news_buttons = []
        self.cache = None
        self.counter = 0
        self.news_b = tk.Button(master, command=CyberNewsTopHeadings.switch)
        self.news_b.pack(pady=10, padx=10)
        print("You are in the CYBER NEWS now!")


class FeedbackForm(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        title_fl = tk.Label(self, text="Feedback Page", font="Helvetica")
        title_fl.pack(pady=10, padx=10)
        nav_fb = tk.Button(self, text="Security Incident", command=lambda: controller.show_frame_type(SecurityIncident))
        nav_fb.pack(pady=10, padx=10)
        print("You are in the FEEDBACK Form now!")


class SecurityIncident(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        title_il = tk.Label(self, text="Security Incident Page", font="Helvetica")
        title_il.pack(pady=10, padx=10)
        nav_ib = tk.Button(self, text="Splash Screen", command=lambda: controller.show_frame_type(SplashScreen))
        nav_ib.pack(pady=10, padx=10)
        print("You are in the SECURITY INCIDENT Form now!")
