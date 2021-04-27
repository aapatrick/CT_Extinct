import tkinter as tk
from PIL import ImageTk, Image
import time


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
        print("You are in the CYBER CHAT now!")


class CyberNews(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        title_nl = tk.Label(self, text="Cyber News", font="Helvetica")
        title_nl.pack(pady=10, padx=10)
        nav_nb = tk.Button(self, text="Feedback", command=lambda: controller.show_frame_type(FeedbackForm))
        nav_nb.pack(pady=10, padx=10)
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


def main():
    # root = tk.Tk()
    # cyber_chatbot = CyberChatbot(root)
    # feedback_form = FeedbackForm(root)
    # cyber_news = CyberNews(root)
    # security_incident = SecurityIncident(root)
    # ct_extinct = CTExtinct(root)
    app = CTExtinct()
    app.mainloop()


if __name__ == "__main__":
    main()
else:
    print('This module cannot be imported or used by another module. Please run code from app.py file')

# class CTExtinct(tk.Tk):
# i used *args and **kwargs here because this is the main class with many features and I do not want to limit its
# functionality. Also to reduce errors as the project increases in size.
#    def __init__(self, *args, **kwargs):
#  __init__ method is the constructor of the class. "self" can be named anything, similar to "this" in Java.
#  *args allows me to add as many arguments/variables as i want when i initialised an instance of class (object)
#  **kwargs allows me to add as many keyword arguments/ dictionaries as I want into the class constructor
#        tk.Tk.__init__(self, *args, **kwargs)
# constructor initialising the tk.TK class (I am overriding it)
#        main_container = tk.Frame(self)  # creating container that will include all frames & widgets of app
#        main_container.pack(side="top", fill="both", expand="True")
#        main_container.grid_rowconfigure(0, weight=1)  # grid_rowconfigure() is a method inherited from the tk.TK class
#        main_container.grid_columnconfigure(0, weight=1)  # "weight" describes the priority, how much space it takes
#        self.frames = {}
#        frame = FeedbackForm(container, self)
#        self.frames[FeedbackForm] = frame
#        frame.grid(row=0, column=0, sticky="nsew")  # sticky property stretches frame in all directions north,South etc.
#        self.show_frame(FeedbackForm)

#    def show_frame(self, cont):
#        frame = self.frames[cont]
#        frame.tkraise()
