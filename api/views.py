from rest_framework import viewsets
from .serializer import MonthSerializer,CateogrySerializer
from .models import Month,Category

# Create your views here.
class MonthViewSet(viewsets.ModelViewSet):
    queryset=Month.objects.all()
    serializer_class= MonthSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class= CateogrySerializer
    