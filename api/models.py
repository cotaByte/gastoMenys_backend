from django.db import models

# Create your models here.
class Month(models.Model):
    id_month= models.PositiveSmallIntegerField()
    name= models.CharField( max_length=50)