from ctextinct.controller import Controller
from ctextinct.model_ import Model

def main():
    training = Model()
    training.training_model()
    #cyber_chatbot = Controller()
    #cyber_chatbot.main()


if __name__ == "__main__":
    main()
else:
    print('This module cannot be imported or used by another module. Please run code from app.py file')
