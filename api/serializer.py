from rest_framework import serializers
from .models import *

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model=Month
        fields=('id_month','name')
        
class CateogrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id_category','name')
        

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__' 