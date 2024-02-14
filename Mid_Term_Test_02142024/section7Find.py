# Find all documents
documents = collection.find()

# Find documents with specific criteria
for document in collection.find({"age": {"$gt": 25}}):
    print(document)
