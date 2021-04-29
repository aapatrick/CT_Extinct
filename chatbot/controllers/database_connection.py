import firebase_admin
from firebase_admin import db
import json


class CTExtinctDatabase:
    def __init__(self):
        self.ref = db.reference("/")  # setting reference to the root of the table
        self.target = {}
        cred_obj = firebase_admin.credentials.Certificate(
            r"../../Assets/files/ctextinct-firebase-adminsdk-xnpem-e13f73b9d2.json")
        default_app = firebase_admin.initialize_app(cred_obj, {
            'databaseURL': "https://ctextinct-default-rtdb.europe-west1.firebasedatabase.app/"
        })

    def write_to_database(self):
        self.ref.set({
            "News":
                {
                    "Article": -1
                }
        })
        self.ref = db.reference("/News/Article")

        # with statement automatically closes the file handler
        with open(r"../../Assets/files/feedback_responses.json", "r") as file_handler:
            file_contents = json.load(file_handler)  # convert json to python dictionary
        print(file_contents)
        for key, value in file_contents.items():
            self.ref.push().set(value)

    def update_database(self):
        self.ref = db.reference("/Books/Best_Sellers/")
        self.target = self.ref.get()
        print(self.target)
        for key, value in self.target.items():
            if value["Author"] == "J.R.R. Tolkien":
                value["Price"] = 90
                self.ref.child(key).update({"Price": 80})

    def retrieve_data_from_database(self):
        self.ref = db.reference("/Books/Best_Sellers/")
        print(self.ref.order_by_child("Price").get())
        self.ref.order_by_child("Price").limit_to_last(1).get()
        self.ref.order_by_child("Price").limit_to_first(1).get()
        self.ref.order_by_child("Price").equal_to(80).get()

    def delete_data_from_database(self):
        self.ref = db.reference("/Books/Best_Sellers")
        for key, value in self.target.items():
            if value["Author"] == "J.R.R. Tolkien":
                self.ref.child(key).set({})
