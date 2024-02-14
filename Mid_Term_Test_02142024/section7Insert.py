# Insert single document
collection.insert_one({"name": "Priyanka", "age": 30})

# Insert multiple documents
documents = [{"name": "Priya", "age": 25}, {"name": "Parisa", "age": 40}]
collection.insert_many(documents)
