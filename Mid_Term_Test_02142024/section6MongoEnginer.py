from mongoengine import connect, Document

# Connect to database
connect("mydatabase")

# Define a document model
class User(Document):
    name = StringField()
    email = EmailField()

# Create and save a document
user = User(name="John Doe", email="johndoe@example.com")
user.save()

# Find documents
users = User.objects.all()
for user in users:
    print(user.name, user.email)
