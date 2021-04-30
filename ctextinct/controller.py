from model_ import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()  # model not aware of controller or view
        self.view = View(self)  # view aware of controller but not model so takes controller as argument
        print("Controller Initialised")

    def main(self):
        self.view.main()  #
        print("Main Controller End")