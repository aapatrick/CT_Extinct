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
        self.controller = controller
        self.input_question = tk.StringVar()  # tk.StringVar helps manage the value of the Entry widget
        self._make_all_frames()
        self._make_output_field()
        self._make_buttons()
        self._make_entry()
        print("View Initialised")

    def main(self):
        self.mainloop()  # allows me to includes events in this application as it creates an infinite loop which can
        # be stopped by closing the window
        print("Main View End.")

    def _make_all_frames(self):
        self.maincontainer = tk.Frame(self)
        self.maincontainer.pack(padx=self.PAD, pady=self.PAD)
        self.input_frame = tk.Frame(self.maincontainer)
        self.input_frame.pack(padx=self.PAD, pady=self.PAD, side="bottom")
        self.nav_frame = tk.Frame(self.maincontainer)
        self.nav_frame.pack(padx=self.PAD, pady=self.PAD)
        self.output_frame = tk.Frame(self.maincontainer)
        self.output_frame.pack(padx=self.PAD, pady=self.PAD, side="top")

    def _make_entry(self):
        chatbot_entry = ttk.Entry(self.input_frame, textvariable=self.input_question, font=self.FONT)
        chatbot_entry.pack(padx=self.PAD, pady=self.PAD, fill="x")

    def _make_output_field(self):
        output_field = tk.Text(self.output_frame, height=20, bg=self.COMPANY_COLOR, fg="white", font=self.FONT)
        output_field.pack(padx=self.PAD, pady=self.PAD, fill="x")

    def _make_buttons(self):
        cyberbot_b = tk.Button(self.nav_frame, text="Cyber Bot", font=self.FONT)
        cybernews_b = tk.Button(self.nav_frame, text="Latest News", font=self.FONT)
        feedback_b = tk.Button(self.nav_frame, text="Feedback Form", font=self.FONT)
        incident_b = tk.Button(self.nav_frame, text="Security Incident", font=self.FONT)
        cyberbot_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        cybernews_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        feedback_b.pack(padx=self.PAD, pady=self.PAD, side="left")
        incident_b.pack(padx=self.PAD, pady=self.PAD, side="left")

# I only used self. when I needed to use that particular variable from outside its method.
# the use of _ at the start  in the naming of a method means that the method wont be called outside the class,
# it is not required, but its meaning is recognised by everyone
