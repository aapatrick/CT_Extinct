import tkinter as tk
import webbrowser

from PIL import ImageTk, Image

from chat import *
from newsApi import *

root = tk.Tk()

root.title("CT Extinct")
root.counter = 0
cache = None
news_buttons = []

root.iconbitmap("../assets/images/individualLogo.ico")
logo_pic = ImageTk.PhotoImage(Image.open("../assets/images/ardonagh.png"))
img_label = tk.Label(root, image=logo_pic)

# if __name__ == "__main__":

def next_question(response):
    entry.delete(0, tk.END)
    responseL.configure(text=response)


def ask_question(event):
    user_q = entry.get()
    ints = predict_tag(user_q)
    response = get_response(ints, intentsDictionary)
    next_question(response)


def visit_news(v):
    webbrowser.open_new_tab(v)


def switch():
    global news_buttons
    if root.counter == 1:
        for i in news_buttons:
            root.news_buttons.remove(root.news_buttons[i])
        root.counter = 0
    if root.counter == 0:
        root.counter = 1
        get_latest_news()


def get_latest_news():
    global cache
    if not cache:
        cache = top_headlines()
    for k, v in cache.items():
        temp = tk.Button(root, text=k, command=lambda: visit_news(v))
        temp.grid(column=1, columnspan=2)
        news_buttons.append(temp)


# tkinter GUI

entry = tk.Entry(root,
                 fg="white",
                 bg="#073529",
                 width=50,
                 borderwidth=10
                 )
responseL = tk.Label(root,
                     text="Janine just joined the chat! What would you like to ask her?",
                     fg="white",
                     bg="#073529",
                     width=50,
                     pady=25,
                     wraplength=300,
                     borderwidth=10,
                     relief="flat"
                     )
news_b = tk.Button(root,
                   text="Latest News",
                   fg="#073529",
                   bg="#D2D0D5",
                   padx=50,
                   pady=25,
                   command=switch,
                   borderwidth=10,
                   relief="solid"
                   )
feedback_b = tk.Button(root,
                       text="Feedback/Complaint",
                       fg="#073529",
                       bg="#D2D0D5",
                       padx=50,
                       pady=25,
                       borderwidth=10,
                       relief="solid"
                       )
securityQ_b = tk.Button(root,
                        text="Ask Security Questions",
                        fg="#073529",
                        bg="#D2D0D5",
                        padx=50,
                        pady=25,
                        borderwidth=10,
                        relief="solid"
                        )
incident_b = tk.Button(root,
                       text="Security Incident",
                       fg="#073529",
                       bg="#D2D0D5",
                       padx=50,
                       pady=25,
                       borderwidth=10,
                       relief="solid"
                       )

testing_label = tk.Label(root,
                         text="testing label" + str(root.counter)
                         )
space_l = tk.Label(root,
                   pady=100,
                   padx=50
                   )
space_l2 = tk.Label(root,
                    pady=50,
                    padx=50
                    )
# testing_label.grid(row=10, column=1, columnspan=2)
root.bind('<Return>', ask_question)
entry.insert(0, "Type your question here")
entry.grid(row=20, column=1, columnspan=2, padx=50, pady=50)
responseL.grid(row=30, column=1, columnspan=2)
space_l.grid(row=50)
space_l2.grid(row=0)
securityQ_b.grid(row=50, column=0)
incident_b.grid(row=50, column=1)
news_b.grid(row=50, column=2)
feedback_b.grid(row=50, column=3)
img_label.grid(row=5, column=1, columnspan=2)
root.mainloop()
