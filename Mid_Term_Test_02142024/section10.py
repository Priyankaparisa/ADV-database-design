# Import the MongoClient class from the pymongo package
from pymongo import MongoClient

# Connect to the MongoDB server running on localhost
client = MongoClient('localhost', 27017)

# Access or create a database named 'mydatabase'
db = client['mydatabase']

# Access or create a collection named 'mycollection' within the 'mydatabase' database
collection = db['mycollection']

# 1. Create (Insert) Operation
# Insert a single document into the collection
document1 = {"name": "Alice", "age": 30, "city": "New York"}
result = collection.insert_one(document1)
print("Inserted document id:", result.inserted_id)

# 2. Read Operation
# Find a document by a specific field value
result = collection.find_one({"name": "Alice"})
print("Found document:", result)

# 3. Update Operation
# Update a document by specifying a filter and the new data
update_filter = {"name": "Alice"}
new_data = {"$set": {"age": 31}}  # Update Alice's age
result = collection.update_one(update_filter, new_data)
print("Updated", result.modified_count, "document")

# 4. Delete Operation
# Delete a document by specifying a filter
delete_filter = {"name": "Alice"}
result = collection.delete_one(delete_filter)
print("Deleted", result.deleted_count, "document")
