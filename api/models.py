from django.db import models

# Create your models here.
class Month(models.Model):
    id_month= models.PositiveSmallIntegerField()
    name= models.CharField( max_length=50)
    
class Category(models.Model):
    id_category= models.PositiveSmallIntegerField()
    name= models.CharField(max_length=50)
    
