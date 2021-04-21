import firebase_admin

cred_obj = firebase_admin.credentials.Certificate(
    r"C:\Users\MrLaziz\Desktop\Kingston University Level 6\Individual "
    r"Project\CT_Extinct\chatbot\ctextinct-firebase-adminsdk-xnpem-e13f73b9d2.json")
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': "https://ctextinct-default-rtdb.europe-west1.firebasedatabase.app/"
})

# WRITE DATA
ref = db.reference("/")
ref.set({
    "News":
        {
            "Article": -1
        }
})

ref = db.reference("/News/Article")
import json

with open(r"C:\Users\MrLaziz\Desktop\Kingston University Level 6\Individual Project\CT_Extinct\chatbot\news.json",
          "r") as f:
    file_contents = json.load(f)

for key, value in file_contents.items():
    ref.push().set(value)

# UPDATE DATA
# ref = db.reference("/Books/Best_Sellers/")
# best_sellers = ref.get()
# print(best_sellers)
# for key, value in best_sellers.items():
#	if(value["Author"] == "J.R.R. Tolkien"):
#		value["Price"] = 90
#		ref.child(key).update({"Price":80})

# RETRIEVE DATA
# ref = db.reference("/Books/Best_Sellers/")
# print(ref.order_by_child("Price").get())
# ref.order_by_child("Price").limit_to_last(1).get()
# ref.order_by_child("Price").limit_to_first(1).get()
# ref.order_by_child("Price").equal_to(80).get()


# DELETE DATA
# ref = db.reference("/Books/Best_Sellers")
# for key, value in best_sellers.items():
#	if(value["Author"] == "J.R.R. Tolkien"):
#		ref.child(key).set({})
