# Import MongoClient class from pymongo package
from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient()

# Access the desired database
db = client.mydatabase

# Access the desired collection
collection = db.mycollection

# Define the filter to identify documents to delete
filter = {"age": {"$gte": 40}}  # Delete documents with age greater than or equal to 40

# Delete a single document matching the filter
result = collection.deleteOne(filter)

# Print the number of documents deleted
print("Number of documents deleted:", result.deleted_count)
