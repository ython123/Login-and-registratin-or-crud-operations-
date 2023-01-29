from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    # This function is used to convert object to string function .
    def __str__(self) -> str:
        return self.fname