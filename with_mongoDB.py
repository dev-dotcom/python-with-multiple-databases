from  pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['TheOffice']  #create database

collection = db['Employees'] #create collection (or table in RDBMS)

# document = {
#     "name" : "Dwight k. Schrute",
#     "designation" : "Salesman",
#     "branch" : "Scranton"
# }
# collection.insert_one(document)       

# documents = [
#     {"name" : "Michael Scott", "designation" : "Regional Manager", "branch" : "Scranton"},
#     {"name" : "Jim Halpert", "designation" : "Salesman", "branch" : "Scranton"},
#     {"name" : "Andrew Bernard", "designation" : "Salesman", "branch" : "Scranton"},
#     {"name" : "Pam Beesley", "designation" : "Salesman", "branch" : "Scranton"},
#     {"name" : "Angela", "designation" : "Accountant", "branch" : "Scranton"},
#     {"name" : "Kevin Malone", "designation" : "Accountant", "branch" : "Scranton"},
#     {"name" : "Oscar", "designation" : "Accountant", "branch" : "Scranton"},
# ]
# collection.insert_many(documents)

print("document inserted")

one = collection.find_one({"name" : "Dwight k. Schrute"})
print(one)

