from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    age = models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<User object: {self.first_name} {self.last_name} {self.id}>"

