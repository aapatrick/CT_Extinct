import tkinter as tk
from tkinter import ttk, END


# The view inherits from tk.Tk() class so I could have access to all its attributes & methods
class View(tk.Tk):
    PAD = 10  # constant, a class variable, which can be different for each instance of this class
    FONT = "helvetica 14"  # reduces repetition and allows me to control font for all my app from one place
    COMPANY_COLOR = "#003428"

    def __init__(self, controller):
        super().__init__()  # super() here is calling the constructor of the tk.Tk object
        self.title("CT Extinct")
        self.iconbitmap("../Assets/Images/individualLogo.ico")
        self.controller = controller
        self.frames_dict = {}
        self.news_buttons = []
        self.input_question = tk.StringVar()  # tk.StringVar helps manage the value of the Entry widget
        self._make_all_frames()
        self._make_output_field()
        self._make_buttons()
        self._make_entry()
        self.bind('<Return>', self.controller.on_enter_key_pressed(self.chatbot_entry.get()))
        print("View Initialised")

    def main(self):
        self.mainloop()  # allows me to includes events in this application as it creates an infinite loop which can
        # be stopped by closing the window
        print("Main View End.")

    def _make_all_frames(self):
        self.maincontainer = tk.Frame(self)
        # setting main container dimensions and making it dynamic with size of window
        self.maincontainer.pack(side="top", padx=self.PAD, pady=self.PAD, fill="both", expand="True")
        tk.Grid.grid_rowconfigure(self.maincontainer, 0, weight=1)
        tk.Grid.grid_columnconfigure(self.maincontainer, 0, weight=1)
        # creating empty dictionary and initialising an instance of each class inside main container
        # then linking them to dictionary keys and positioning them so they can fill the whole window
        self.splash_frame = tk.Frame(self.maincontainer)
        self.cyber_bot_frame = tk.Frame(self.maincontainer)
        self.cyber_news_frame = tk.Frame(self.maincontainer)
        self.feedback_form_frame = tk.Frame(self.maincontainer)
        self.cyber_incident_frame = tk.Frame(self.maincontainer)
        self.splash_frame.grid(row=0, column=0, sticky="nsew")
        self.cyber_bot_frame.grid(row=0, column=0, sticky="nsew")
        self.cyber_news_frame.grid(row=0, column=0, sticky="nsew")
        self.feedback_form_frame.grid(row=0, column=0, sticky="nsew")
        self.cyber_incident_frame.grid(row=0, column=0, sticky="nsew")
        self.frames_dict["splash_frame"] = self.splash_frame
        self.frames_dict["cyber_bot_frame"] = self.cyber_bot_frame
        self.frames_dict["cyber_news_frame"] = self.cyber_news_frame
        self.frames_dict["feedback_form_frame"] = self.feedback_form_frame
        self.frames_dict["cyber_incident_frame"] = self.cyber_incident_frame

        # Cyber_Bot Frame
        self.input_frame = tk.Frame(self.cyber_bot_frame)
        self.input_frame.pack(padx=self.PAD, pady=self.PAD, side="bottom")
        self.nav_frame = tk.Frame(self.cyber_bot_frame)
        self.nav_frame.pack(padx=self.PAD, pady=self.PAD)
        self.output_frame = tk.Frame(self.cyber_bot_frame)
        self.output_frame.pack(padx=self.PAD, pady=self.PAD, side="top")
        # Cyber_News Frame

        # showing the Splash page first
        self.controller.show_frame_type("splash_frame")

    def delete_news_buttons(self):
        for i in range((len(self.news_buttons)-1)):
            self.news_buttons.remove(self.news_buttons[i])

    def create_news_buttons(self):
        for k, v in self.cache.items():
            temp = tk.Button(self, text=k, command=lambda: self.controller.visit_news(v))
            temp.pack(pady=10, padx=10)
            self.news_buttons.append(temp)

    def _make_entry(self):
        self.chatbot_entry = ttk.Entry(self.input_frame, textvariable=self.input_question, font=self.FONT)
        self.chatbot_entry.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")

    def _make_output_field(self):
        self.output_field = tk.Text(self.output_frame, height=20, bg=self.COMPANY_COLOR,
                                    fg="white", font=self.FONT, state="disabled")
        self.output_field.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")

    def _make_buttons(self):
        self.cyberbot_b = tk.Button(self.nav_frame, text="Cyber Bot", font=self.FONT,
                                    command=lambda: self.controller.on_button_click("Cyber Bot"))
        self.cybernews_b = tk.Button(self.nav_frame, text="Latest News", font=self.FONT,
                                     command=lambda: self.controller.on_button_click("Latest News"))
        self.feedback_b = tk.Button(self.nav_frame, text="Feedback Form", font=self.FONT,
                                    command=lambda: self.controller.on_button_click("Feedback Form"))
        self.incident_b = tk.Button(self.nav_frame, text="Security Incident", font=self.FONT,
                                    command=lambda: self.controller.on_button_click("Security Incident"))
        self.cyberbot_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        self.cybernews_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        self.feedback_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        self.incident_b.pack(padx=self.PAD, pady=self.PAD, side="left")

        for button in self.news_buttons:
            self.news_buttons = tk.Button(self.cyber_news_frame, text="Latest News", font=self.FONT,
                                     command=lambda: self.controller.on_button_click("Latest News"))

    def next_question(self, response):
        self.chatbot_entry.delete(0, END)
        self.output_field.configure(text=response)

    def visit_splash_screen(self):
        title_sl = tk.Label(self, text="SPLASH SCREEN", font="Helvetica")
        title_sl.pack(pady=10, padx=10)
        nav_sb = tk.Button(self, text="Cyber Chat",
                           command=lambda: self.controller.show_frame_type(self.cyber_bot_frame))
        nav_sb.pack(pady=10, padx=10)
        print("You are in the SPLASH SCREEN now!")

    def visit_cyber_bot(self):
        chat_ci = tk.Entry(self)
        chat_ci.pack(pady=10, padx=10)
        nav_cb = tk.Button(self, text="Cyber News",
                           command=lambda: self.controller.show_frame_type(self.cyber_news_frame))
        nav_cb.pack(pady=10, padx=10)
        self.entry = tk.Entry(master)
        self.responseL = tk.Label(master, text="Janine just joined the chat! What would you like to ask her?")
        self.securityQ_b = tk.Button(master, text="Ask Security Questions")
        self.master.bind('<Return>', self.ask_question())
        self.entry.pack(row=20, column=1, columnspan=2)
        self.responseL.pack(pady=10, padx=10)(row=30, column=1, columnspan=2)
        self.securityQ_b.pack(pady=10, padx=10)

    def visit_cyber_news(self):
        self.master = master
        title_nl = tk.Label(self, text="Cyber News", font="Helvetica")
        title_nl.pack(pady=10, padx=10)
        nav_nb = tk.Button(self, text="Feedback",
                           command=lambda: self.controller.show_frame_type(self.feedback_form_frame))
        nav_nb.pack(pady=10, padx=10)
        self.news_buttons = []
        self.cache = None
        self.counter = 0
        self.news_b = tk.Button(master, command=self.controller.switch_news_button)
        self.news_b.pack(pady=10, padx=10)
        print("You are in the CYBER NEWS now!")

    def visit_feedback_form(self):
        title_fl = tk.Label(self, text="Feedback Page", font="Helvetica")
        title_fl.pack(pady=10, padx=10)
        nav_fb = tk.Button(self, text="Security Incident",
                           command=lambda: self.controller.show_frame_type(self.cyber_incident_frame))
        nav_fb.pack(pady=10, padx=10)
        print("You are in the FEEDBACK Form now!")

    def visit_security_incident(self):
        title_il = tk.Label(self, text="Security Incident Page", font="Helvetica")
        title_il.pack(pady=10, padx=10)
        nav_ib = tk.Button(self, text="Splash Screen",
                           command=lambda: self.controller.show_frame_type(self.splash_frame))
        nav_ib.pack(pady=10, padx=10)
        print("You are in the SECURITY INCIDENT Form now!")

# I only used self. when I needed to use that particular variable from outside its method.
# the use of _ at the start  in the naming of a method means that the method wont be called outside the class,
# it is not required, it is a convention and  is recognised by everyone
