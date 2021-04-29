import tkinter as tk
from chatbot.views.main_view import SplashScreen, CyberChatbot, FeedbackForm, CyberNews


#  CTExtinct(tk.TK): inherit from tk.TK class within tkinter
class CTExtinct(tk.Tk):
    # i used *args and **kwargs here because this is the main class with many features and I do not want to limit its
    # functionality. Also to reduce errors as the project increases in size.
    def __init__(self, *args, **kwargs):
        #  __init__ method is the constructor of the class. "self" can be named anything, similar to "this" in Java.
        #  *args allows me to add as many arguments/variables as i want when i initialised an instance of class (object)
        #  **kwargs allows me to add as many keyword arguments/ dictionaries as I want into the class constructor
        tk.Tk.__init__(self, *args, **kwargs)
        # constructor initialising the tk.TK class (I am overriding it)
        main_container = tk.Frame(self)
        # setting main container dimensions and making it dynamic with size of window
        main_container.pack(side="top", fill="both", expand="True")
        tk.Grid.grid_rowconfigure(main_container, 0, weight=1)
        tk.Grid.grid_columnconfigure(main_container, 0, weight=1)
        # creating empty dictionary and initialising an instance of each class inside main container
        # then linking them to dictionary keys and positioning them so they can fill the whole window
        self.frames_dict = {}
        for class_frame in (SplashScreen, CyberChatbot, FeedbackForm, CyberNews):
            temp = class_frame(main_container, self)
            self.frames_dict[class_frame] = temp
            temp.grid(row=0, column=0, sticky="nsew")
        # showing the Splash page
        self.show_frame_type(SplashScreen)
        print("You are in the CTEXTINCT Main container now!")

    def show_frame_type(self, frame_type):
        visible_frame = self.frames_dict[frame_type]
        visible_frame.tkraise()
