import tkinter as tk
from tkinter import ttk


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
        self.frames_dict = {}
        for class_frame in (SplashScreen, CyberChatbot, FeedbackForm, CyberNews):
            temp = class_frame(main_container, self)
            self.frames_dict[class_frame] = temp
            temp.grid(row=0, column=0, sticky="nsew")
        self.input_frame = tk.Frame(self.maincontainer)
        self.input_frame.pack(padx=self.PAD, pady=self.PAD, side="bottom")
        self.nav_frame = tk.Frame(self.maincontainer)
        self.nav_frame.pack(padx=self.PAD, pady=self.PAD)
        self.output_frame = tk.Frame(self.maincontainer)
        self.output_frame.pack(padx=self.PAD, pady=self.PAD, side="top")
        # showing the Splash page first
        self.show_frame_type(SplashScreen)

    def _make_entry(self):
        chatbot_entry = ttk.Entry(self.input_frame, textvariable=self.input_question, font=self.FONT)
        chatbot_entry.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")

    def _make_output_field(self):
        output_field = tk.Text(self.output_frame, height=20, bg=self.COMPANY_COLOR,
                               fg="white", font=self.FONT, state="disabled")
        output_field.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")

    def _make_buttons(self):
        cyberbot_b = tk.Button(self.nav_frame, text="Cyber Bot", font=self.FONT,
                               command=lambda: self.controller.on_button_click("Cyber Bot"))
        cybernews_b = tk.Button(self.nav_frame, text="Latest News", font=self.FONT,
                                command=lambda: self.controller.on_button_click("Latest News"))
        feedback_b = tk.Button(self.nav_frame, text="Feedback Form", font=self.FONT,
                               command=lambda: self.controller.on_button_click("Feedback Form"))
        incident_b = tk.Button(self.nav_frame, text="Security Incident", font=self.FONT,
                               command=lambda: self.controller.on_button_click("Security Incident"))
        cyberbot_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        cybernews_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        feedback_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        incident_b.pack(padx=self.PAD, pady=self.PAD, side="left")



    def visit_splash_screen(self):
        tk.Frame.__init__(self, master)
        title_sl = tk.Label(self, text="SPLASH SCREEN", font="Helvetica")
        title_sl.pack(pady=10, padx=10)
        nav_sb = tk.Button(self, text="Cyber Chat", command=lambda: controller.show_frame_type(CyberChatbot))
        nav_sb.pack(pady=10, padx=10)
        print("You are in the SPLASH SCREEN now!")

    def visit_cyber_bot(self):
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

    def visit_cyber_news(self):
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

    def visit_feedback_form(self):
        tk.Frame.__init__(self, master)
        title_fl = tk.Label(self, text="Feedback Page", font="Helvetica")
        title_fl.pack(pady=10, padx=10)
        nav_fb = tk.Button(self, text="Security Incident",
                           command=lambda: controller.show_frame_type(SecurityIncident))
        nav_fb.pack(pady=10, padx=10)
        print("You are in the FEEDBACK Form now!")

    def visit_security_incident(self):
        title_il = tk.Label(self, text="Security Incident Page", font="Helvetica")
        title_il.pack(pady=10, padx=10)
        nav_ib = tk.Button(self, text="Splash Screen", command=lambda: self.controller.show_frame_type(SplashScreen))
        nav_ib.pack(pady=10, padx=10)
        print("You are in the SECURITY INCIDENT Form now!")



# I only used self. when I needed to use that particular variable from outside its method.
# the use of _ at the start  in the naming of a method means that the method wont be called outside the class,
# it is not required, it is a convention and  is recognised by everyone
