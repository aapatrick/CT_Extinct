import tkinter as tk
from tkinter import ttk, END, CENTER
from PIL import ImageTk, Image
import time


class Splash(tk.Toplevel):
    def __init__(self, main_window):
        tk.Toplevel.__init__(self, main_window)
        self.wm_attributes('-fullscreen', 'true')
        logo_img = Image.open("../Assets/Images/transparent_ardonagh.png")
        logo_img = logo_img.resize((562, 202), Image.ANTIALIAS)
        splash_logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(self, image=splash_logo)
        logo_label.image = splash_logo
        logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        # required to make window show before the program gets to the mainloop
        self.update()


# The view inherits from tk.Tk() class so I could have access to all its attributes & methods
class View(tk.Tk):
    PAD = 10  # constant, a class variable, which can be different for each instance of this class
    FONT = "helvetica 14"  # reduces repetition and allows me to control font for all my app from one place
    COMPANY_COLOR = "#003428"

    def __init__(self, controller):
        super().__init__()  # super() here is calling the constructor of the tk.Tk object
        # remove main_window
        self.withdraw()
        # show splash screen
        splash_screen = Splash(self)
        # setup Main Window
        self.controller = controller
        self.frames_dict = {}
        self.news_buttons = []
        self.nav = False
        # simulating a delay while loading
        time.sleep(3)
        # loading finished so splash screen destroyed
        splash_screen.destroy()
        # show main_window again
        self.deiconify()
        print("View Initialised")

    def main(self):
        self.title("CT Extinct")
        self.iconbitmap("../Assets/Images/individualLogo.ico")
        app_width = 750
        app_height = 650
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self._make_all_frames()
        self._make_cyber_news_widgets()
        self._make_cyber_bot_widgets()
        self.show_frame_type("cyber_bot_frame")
        self.chatbot_entry.bind('<Return>', self.controller.on_enter_key_pressed(self.chatbot_entry.get()))
        self.mainloop()  # allows me to includes events in this application as it creates an infinite loop which can
        # be stopped by closing the window

    def _make_all_frames(self):
        self.maincontainer = tk.Frame(self, bg="black")
        self.maincontainer.pack(side="top", fill="both", expand="True")
        # setting main container dimensions and making it dynamic with size of window
        tk.Grid.grid_rowconfigure(self.maincontainer, 0, weight=1)
        tk.Grid.grid_columnconfigure(self.maincontainer, 0, weight=1)
        # creating empty dictionary and initialising an instance of each class inside main container
        # then linking them to dictionary keys and positioning them so they can fill the whole window
        self.cyber_bot_frame = tk.Frame(self.maincontainer, bg="blue")
        self.cyber_news_frame = tk.Frame(self.maincontainer, bg="black")
        self.feedback_form_frame = tk.Frame(self.maincontainer, bg="red")
        self.cyber_incident_frame = tk.Frame(self.maincontainer, bg="yellow")
        self.cyber_bot_frame.grid(row=0, column=0, sticky="nsew")
        self.cyber_news_frame.grid(row=0, column=0, sticky="nsew")
        self.feedback_form_frame.grid(row=0, column=0, sticky="nsew")
        self.cyber_incident_frame.grid(row=0, column=0, sticky="nsew")
        # self.frames_dict["splash_frame"] = self.splash_frame
        self.frames_dict["cyber_bot_frame"] = self.cyber_bot_frame
        self.frames_dict["cyber_news_frame"] = self.cyber_news_frame
        self.frames_dict["feedback_form_frame"] = self.feedback_form_frame
        self.frames_dict["cyber_incident_frame"] = self.cyber_incident_frame
        # nav frame
        self.nav_frame1 = tk.Frame(self.cyber_bot_frame, bg="blue")
        self.nav_frame2 = tk.Frame(self.cyber_news_frame, bg="blue")
        self.nav_frame3 = tk.Frame(self.feedback_form_frame, bg="blue")
        self.nav_frame4 = tk.Frame(self.cyber_incident_frame, bg="blue")
        self.nav_frame1.pack(padx=self.PAD, pady=self.PAD)
        self.nav_frame2.pack(padx=self.PAD, pady=self.PAD)
        self.nav_frame3.pack(padx=self.PAD, pady=self.PAD)
        self.nav_frame4.pack(padx=self.PAD, pady=self.PAD)

    def create_menu(self):
        main_menu = tk.Menu(self)
        self.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(Label="File", menu=file_menu)
        file_menu.add_command(Label="Sign Out", command=self.controller.restart_program())
        file_menu.add_separator()
        file_menu.add_command(Label="Exit", command=self.controller.restart_program())

        navigate_menu = tk.Menu(main_menu)
        main_menu.add_cascade(Label="Navigate To", menu=navigate_menu)
        navigate_menu.add_command(Label="Cyber Bot", command=lambda: self.show_frame_type("cyber_bot_frame"))
        navigate_menu.add_separator()
        navigate_menu.add_command(Label="Cyber News", command=lambda: self.show_frame_type("cyber_news_frame"))
        navigate_menu.add_separator()
        navigate_menu.add_command(Label="Feedback Form", command=lambda: self.show_frame_type("feedback_form_frame"))
        navigate_menu.add_separator()
        navigate_menu.add_command(Label="Security Incident", command=lambda: self.show_frame_type("cyber_incident_frame"))

        help_menu = tk.Menu(main_menu)
        main_menu.add_cascade(Label="Help", menu=help_menu)
        help_menu.add_command(Label="Help on Our Site",
                              command=self.controller.visit_site("https://kunet.kingston.ac.uk/k1739510/ctExtinct"
                                                                 "/view/index.php"))
        help_menu.add_separator()
        help_menu.add_command(Label="Version", command=print("Version 1.0"))

    def show_frame_type(self, frame_type):
        visible_frame = self.frames_dict[frame_type]
        if frame_type == "cyber_news_frame":
            self.controller.on_button_click("news_b")
        self._make_nav_buttons(visible_frame)
        visible_frame.tkraise()

    def delete_news_buttons(self):
        for i in range((len(self.news_buttons) - 1)):
            self.news_buttons.remove(self.news_buttons[i])

    def create_news_buttons(self):
        for k, v in self.cache.items():
            temp = tk.Button(self.cyber_news_frame, text=k, command=lambda: self.controller.visit_site(v))
            temp.pack(pady=self.PAD, padx=self.PAD)
            self.news_buttons.append(temp)

    def _make_cyber_bot_widgets(self):
        self.input_frame = tk.Frame(self.cyber_bot_frame, bg="yellow")
        self.output_frame = tk.Frame(self.cyber_bot_frame, bg="red")
        self.output_frame.pack(padx=self.PAD, pady=self.PAD, side="top")
        self.input_frame.pack(padx=self.PAD, pady=self.PAD, side="bottom")

        self.chatbot_entry = tk.Entry(self.input_frame, font=self.FONT)
        self.output_field = tk.Label(self.output_frame,
                                     text="Chatbot: Hey my name is Janine, you can ask me anything relating to Cyber "
                                          "Security",
                                     height=20,
                                     bg=self.COMPANY_COLOR, wraplength=700, justify="left", fg="white", font=self.FONT)
        self.chatbot_entry.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")
        self.output_field.pack(padx=self.PAD, pady=self.PAD, fill="both", expand="True")

    def _make_cyber_news_widgets(self):
        title_l = tk.Label(self.cyber_news_frame, text="Top 20 Cyber Headlines")
        title_l.pack(padx=self.PAD, pady=self.PAD)

    def _make_nav_buttons(self, frame):
        self.nav_frame = tk.Frame(frame, bg="blue")
        self.nav_frame.pack(padx=self.PAD, pady=self.PAD)
        if not self.nav:
            self.cyberbot_b = tk.Button(self.nav_frame, text="Cyber Bot", font=self.FONT,
                                        command=lambda: self.show_frame_type("cyber_bot_frame"))
            self.cybernews_b = tk.Button(self.nav_frame, text="Latest News", font=self.FONT,
                                         command=lambda: self.show_frame_type("cyber_news_frame"))
            self.feedback_b = tk.Button(self.nav_frame, text="Feedback Form", font=self.FONT,
                                        command=lambda: self.show_frame_type("feedback_form_frame"))
            self.incident_b = tk.Button(self.nav_frame, text="Security Incident", font=self.FONT,
                                        command=lambda: self.show_frame_type("cyber_incident_frame"))
            self.logout_b = tk.Button(self.nav_frame, text="Logout", font=self.FONT,
                                      command=lambda: self.controller.restart_program())
            self.cyberbot_b.pack(padx=self.PAD, pady=self.PAD, side="left")
            self.cybernews_b.pack(padx=self.PAD, pady=self.PAD, side="left")
            self.feedback_b.pack(padx=self.PAD, pady=self.PAD, side="left")
            self.incident_b.pack(padx=self.PAD, pady=self.PAD, side="left")
            self.logout_b.pack(padx=self.PAD, pady=self.PAD, side="left")
            self.nav = True

    def next_question(self, response):
        self.chatbot_entry.delete(0, END)
        self.output_field.configure(text=response)

# I only used self. when I needed to use that particular variable from outside its method.
# the use of _ at the start  in the naming of a method means that the method wont be called outside the class,
# it is not required, it is a convention and  is recognised by everyone
