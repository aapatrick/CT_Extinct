import tkinter as tk


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
