import tkinter as tk
import webbrowser

from PIL import ImageTk, Image

from chat import *
from newsApi import *

root = tk.Tk()
root.grid(padx=20, pady=20)
root.title("CT Extinct")
root.counter = 0
cache = None
news_buttons = []

root.iconbitmap("../assets/images/individualLogo.ico")


# logo_pic = ImageTk.PhotoImage(Image.open("../assets/images/individualLogo.png"))
# img_label = tk.Label(root, image=logo_pic)


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
                 fg="yellow",
                 bg="green",
                 width=50,
                 borderwidth=10
                 )
responseL = tk.Label(root,
                     text="Janine just joined the chat! What would you like to ask her?",
                     fg="yellow",
                     bg="green",
                     )
news_b = tk.Button(root,
                   text="Latest News",
                   fg="red",
                   bg="black",
                   padx=50,
                   pady=25,
                   command=switch
                   )
feedback_b = tk.Button(root,
                       text="Feedback/Complaint",
                       fg="red",
                       bg="black",
                       padx=50,
                       pady=25
                       )
securityQ_b = tk.Button(root,
                        text="Ask Security Questions",
                        fg="red",
                        bg="black",
                        padx=50,
                        pady=25
                        )
incident_b = tk.Button(root,
                       text="Security Incident",
                       fg="red",
                       bg="black",
                       padx=50,
                       pady=25
                       )

testing_label = tk.Label(root,
                         text="testing label" + str(root.counter)
                         )
testing_label.grid(row=1, column=1, columnspan=2)
root.bind('<Return>', ask_question)
entry.insert(0, "Type your question here")
entry.grid(row=2, column=1, columnspan=2, padx=50, pady=50)
responseL.grid(row=3, column=1, columnspan=2)
securityQ_b.grid(row=4, column=0)
incident_b.grid(row=4, column=1)
news_b.grid(row=4, column=2)
feedback_b.grid(row=4, column=3)

# img_label.grid(row=10, column=10)
root.mainloop()
