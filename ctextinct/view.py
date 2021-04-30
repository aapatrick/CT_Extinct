import tkinter as tk
from tkinter import ttk


# The view inherits from tk.Tk() class so I could have access to all its attributes & methods
class View(tk.Tk):
    PAD = 10  # constant that can be different for each instance of the class

    def __init__(self, controller):
        super().__init__()  # super() here is calling the constructor of the tk.Tk object
        self.title("CT Extinct")
        self.controller = controller
        self.input_question = tk.StringVar()  # tk.StringVar helps manage the value of the Entry widget
        self._make_main_frame()
        self._make_entry()
        print("View Initialised")

    def main(self):
        self.mainloop()  # allows me to includes events in this application as it creates an infinite loop which can
        # be stopped by closing the window
        print("Main View End.")

    def _make_main_frame(self):
        self.maincontainer = tk.Frame(self)
        self.maincontainer.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        chatbot_entry = ttk.Entry(self.maincontainer, textvariable=self.input_question)
        chatbot_entry.pack(padx=self.PAD, pady=self.PAD)

# I only used self. when I needed to use that particular variable from outside its method.
