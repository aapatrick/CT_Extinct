from model_ import Model
from view import View


class Controller:

    frames_dict = {self.view.nav_frame, }

    # i used *args and **kwargs here because this is the main class with many features and I do not want to limit its
    # functionality. Also to reduce errors as the project increases in size.
    def __init__(self, *args, **kwargs):
        #  __init__ method is the constructor of the class. "self" can be named anything, similar to "this" in Java.
        #  *args allows me to add as many arguments/variables as i want when i initialised an instance of class (object)
        #  **kwargs allows me to add as many keyword arguments/ dictionaries as I want into the class constructor
        self.model = Model()  # model not aware of controller or view
        self.view = View(self)  # view aware of controller but not model so takes controller as argument
        print("Controller Initialised")

    def main(self):
        self.view.main()  #
        print("Main Controller End")

    def on_button_click(self, button_name):
        print(f"button {button_name} clicked")

    def on_enter_key_pressed(self, user_question):
        response = self.model.ask_question(user_question)
        self.model.next_question(response)

    def show_frame_type(self, frame_type):
        visible_frame = self.frames_dict[frame_type]
        visible_frame.tkraise()

    def submit_feedback_form(self):
        pass

    def submit_cyber_incident(self):
        pass

    def grab_top_twenty_news_headlines(self):
        pass

    def train_model(self):
        pass

    def parse_cyber_security_forum_and_replace_training_data(self):
        pass