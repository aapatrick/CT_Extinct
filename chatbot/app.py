from chat import *
import tkinter as tk


# if __name__ == "__main__":

def next_question(response):
    print("error 1")
    entry.delete(0, tk.END)
    print("error 2")
    responseL.configure(text=response)
    print("error 3")


def ask_question(Event):
    print("firstaskquestion")
    user_q = entry.get()
    print("firstaskquestion2")
    ints = predict_tag(user_q)
    print("firstaskquestion3")
    response = get_response(ints, intentsDictionary)
    print("firstaskquestion4")
    next_question(response)


# tkinter GUI
root = tk.Tk()
entry = tk.Entry(
    fg="yellow",
    bg="green",
    width=50
)
responseL = tk.Label(
    text="Janine just joined the chat! What would you like to ask her?",
    fg="yellow",
    bg="green",
)
root.bind('<Return>', ask_question)
entry.pack()
responseL.pack()
root.mainloop()
