from django.db import models

# Create your models here.
class Contact(models.Model):
  Name=models.CharField(max_length=50,null="true")
  email=models.CharField(max_length=50)
  text=models.TextField(max_length=100)
  date=models.DateField()


