import tkinter as tk
from tkinter import ttk, END, CENTER
from PIL import ImageTk, Image


# The view inherits from tk.Tk() class so I could have access to all its attributes & methods
class View(tk.Tk):
    PAD = 10  # constant, a class variable, which can be different for each instance of this class
    FONT = "helvetica 14"  # reduces repetition and allows me to control font for all my app from one place
    COMPANY_COLOR = "#003428"

    def __init__(self, controller):
        super().__init__()  # super() here is calling the constructor of the tk.Tk object
        self.controller = controller
        self.title("CT Extinct")
        self.iconbitmap("../Assets/Images/individualLogo.ico")
        self.frames_dict = {}
        self.news_buttons = []
        print("View Initialised")

    def main(self):
        self._make_all_frames()
        self._make_output_field()
        self._make_buttons()
        self._make_entry()
        self.bind('<Return>', self.controller.on_enter_key_pressed(self.chatbot_entry.get()))
        self.mainloop()  # allows me to includes events in this application as it creates an infinite loop which can
        # be stopped by closing the window

    def _make_all_frames(self):
        self.maincontainer = tk.Frame(self, bg="black")
        # setting main container dimensions and making it dynamic with size of window
        tk.Grid.grid_rowconfigure(self.maincontainer, 0, weight=1)
        tk.Grid.grid_columnconfigure(self.maincontainer, 0, weight=1)
        # creating empty dictionary and initialising an instance of each class inside main container
        # then linking them to dictionary keys and positioning them so they can fill the whole window
        self.splash_frame = tk.Frame(self.maincontainer, bg="#F0F0F0")
        self.cyber_bot_frame = tk.Frame(self.maincontainer, bg="blue")
        self.cyber_news_frame = tk.Frame(self.maincontainer, bg="black")
        self.feedback_form_frame = tk.Frame(self.maincontainer, bg="red")
        self.cyber_incident_frame = tk.Frame(self.maincontainer, bg="yellow")
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

        # Splash Frame
        logo_img = Image.open("../Assets/Images/transparent_ardonagh.png")
        logo_img = logo_img.resize((562, 202), Image.ANTIALIAS)
        splash_logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(self.splash_frame, image=splash_logo)
        logo_label.image = splash_logo
        logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Cyber_Bot Frame
        self.input_frame = tk.Frame(self.cyber_bot_frame, bg="yellow")
        self.nav_frame = tk.Frame(self.cyber_bot_frame, bg="green")
        self.output_frame = tk.Frame(self.cyber_bot_frame, bg="red")
        self.show_news_frame = tk.Frame(self.cyber_news_frame, bg="blue")

        self.maincontainer.pack(side="top", fill="both", expand="True")
        self.output_frame.pack(padx=self.PAD, pady=self.PAD, side="top")
        self.nav_frame.pack(padx=self.PAD, pady=self.PAD)
        self.input_frame.pack(padx=self.PAD, pady=self.PAD, side="bottom")
        self.show_news_frame.pack(padx=self.PAD, pady=self.PAD)

        # showing the Splash page first
        self.show_frame_type("splash_frame")

    def show_frame_type(self, frame_type):
        visible_frame = self.frames_dict[frame_type]
        visible_frame.tkraise()

    def delete_news_buttons(self):
        for i in range((len(self.news_buttons) - 1)):
            self.news_buttons.remove(self.news_buttons[i])

    def create_news_buttons(self):
        for k, v in self.cache.items():
            temp = tk.Button(self, text=k, command=lambda: self.controller.visit_news(v))
            temp.pack(pady=self.PAD, padx=self.PAD)
            self.news_buttons.append(temp)

    def _make_entry(self):
        self.chatbot_entry = tk.Entry(self.input_frame, font=self.FONT)
        self.chatbot_entry.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")

    def _make_output_field(self):
        self.output_field = tk.Label(self.output_frame,
                                     text="Chatbot: Hey my name is Janine, you can ask me anything relating to Cyber "
                                          "Security",
                                     height=20,
                                     bg=self.COMPANY_COLOR, wraplength=700, justify="left", fg="white", font=self.FONT)
        self.output_field.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")

    def _make_buttons(self):
        self.cyberbot_b = tk.Button(self.nav_frame, text="Cyber Bot", font=self.FONT,
                                    command=lambda: self.show_frame_type("cyber_bot_frame"))
        self.cybernews_b = tk.Button(self.nav_frame, text="Latest News", font=self.FONT,
                                     command=lambda: self.show_frame_type("cyber_news_frame"))
        self.feedback_b = tk.Button(self.nav_frame, text="Feedback Form", font=self.FONT,
                                    command=lambda: self.show_frame_type("feedback_form_frame"))
        self.incident_b = tk.Button(self.nav_frame, text="Security Incident", font=self.FONT,
                                    command=lambda: self.show_frame_type("cyber_incident_frame"))
        self.reset_b = tk.Button(self.nav_frame, text="Logout", font=self.FONT,
                                 command=lambda: self.show_frame_type("splash_frame"))
        self.cyberbot_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        self.cybernews_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        self.feedback_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        self.incident_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        self.reset_b.pack(padx=self.PAD, pady=self.PAD, side="left")

    def next_question(self, response):
        self.chatbot_entry.delete(0, END)
        self.output_field.configure(text=response)

# I only used self. when I needed to use that particular variable from outside its method.
# the use of _ at the start  in the naming of a method means that the method wont be called outside the class,
# it is not required, it is a convention and  is recognised by everyone
