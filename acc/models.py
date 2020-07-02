from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name
