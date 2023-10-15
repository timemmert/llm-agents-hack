import pymongo

# Replace this with your MongoDB connection URI
mongo_uri = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)

db = client["mydb"]


collection = db["mycollection"]


data = {"name": "John"}
collection.insert_one(data)

# Insert multiple documents
data_list = [
    {"name": "Alice"},
    {"name": "Bob"}
]
collection.insert_many(data_list)

result = collection.find({"name": "Alice"})

for document in result:
    print(document)

client.drop_database("mydb")


