from django.db import models
from uuid import uuid4

# Create your models here.
class Month(models.Model):
    id_month= models.PositiveSmallIntegerField()
    name= models.CharField( max_length=50)
    
class Category(models.Model):
    id_category= models.PositiveSmallIntegerField()
    name= models.CharField(max_length=50)
    
class Transaction(models.Model):
    
    TRANSACTION_TYPE_OPTIONS=[
        ('income','Income'),
        ('expense','Expense')
    ]
    
    id_transaction= models.UUIDField(default=uuid4(), editable=False)
    id_category= models.ForeignKey(Category, on_delete=models.CASCADE)
    date= models.DateField()
    description= models.CharField(max_length=100)
    quantity= models.FloatField()
    comments=models.CharField(max_length=150)
    type_transaction= models.CharField(max_length=7,choices=TRANSACTION_TYPE_OPTIONS)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField()