from django.db import models


# Create your models here.
class Member(models.Model):
    """The project model with firstname, lastname, message and date data and returns firstname and lastname."""
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date = models.DateField()
    message = models.CharField(max_length=255)
    
    def __str__(self):
        """Returns the firstname and lastname"""
        return f"{self.firstname} {self.lastname}"