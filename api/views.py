from rest_framework import viewsets
from .serializer import MonthSerializer
from .models import Month

# Create your views here.
class MonthViewSet(viewsets.ModelViewSet):
    queryset=Month.objects.all()
    serializer_class= MonthSerializer
    