from rest_framework import serializers
from .models import Month,Category

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model=Month
        fields=('id_month','name')
        
class CateogrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id_category','name')
        
        