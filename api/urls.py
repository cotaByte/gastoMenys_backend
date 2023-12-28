from django.urls import path, include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'months',views.MonthViewSet)
router.register(r'categories',views.CategoryViewSet)
router.register(r'transactions',views.TransactionViewSet)
router.register(r'users',views.UserViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('getTransactionsByMonth/<str:user_id>/<int:year>/<int:month>/', views.TransactionListView.as_view())
]
