from rest_framework import viewsets
from .serializer import *
from .models import *
import calendar
from datetime import datetime, timedelta
from django.views import View
from django.http import JsonResponse

class MonthViewSet(viewsets.ModelViewSet):
    queryset=Month.objects.all()
    serializer_class= MonthSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class= CateogrySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class= TransactionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer

class TransactionListView(View):
    serializer_class = TransactionSerializer
    def get(self, request, user_id,year, month):
        transactions = Transaction.objects.filter(date__year=year, date__month=month,user_id=user_id)
        serialized_data = self.serializer_class(transactions, many=True).data
        return JsonResponse({'transactions': serialized_data})