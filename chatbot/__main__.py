from chatbot.controllers.main_screen_controller import CTExtinct
from chatbot.models.training import TrainChatbot


def main():
    # train_chatbot = TrainChatbot("../Assets/files/intents.json")
    app = CTExtinct()
    app.mainloop()


if __name__ == "__main__":
    main()
else:
    print('This module cannot be imported or used by another module. Please run code from app.py file')
