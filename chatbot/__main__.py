from chatbot.controllers.main_screen_controller import CTExtinct


def main():
    app = CTExtinct()
    app.mainloop()


if __name__ == "__main__":
    main()
else:
    print('This module cannot be imported or used by another module. Please run code from app.py file')
