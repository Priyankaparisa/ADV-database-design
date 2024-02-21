from pymongo import MongoClient

# Replace placeholders with your details
client = MongoClient("localhost", 27017)
db = client["mydatabase"]
collection = db["mycollection"]

# Access data
for document in collection.find():
    print(document)

# Close connection
client.close()
