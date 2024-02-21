# Import MongoClient class from pymongo package
from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient()

# Access the desired database
db = client.mydatabase

# Access the desired collection
collection = db.mycollection

# Define the filter to identify the document to replace
filter = {"name": "Priya"}

# Define the new document with updated fields
new_document = {
    "name": "Priya",
    "age": 35,
    "city": "HArtford"
}

# Replace the existing document with the new one
result = collection.replaceOne(filter, new_document)

# Print the number of documents replaced
print("Number of documents replaced:", result.modified_count)
