from django.db import models

# Connect to database
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "mydatabase",
    }
}

# Define a Django model
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

# Access data using Django ORM
users = User.objects.all()
for user in users:
    print(user.name, user.email)
