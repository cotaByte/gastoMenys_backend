from django.urls import path, include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'months',views.MonthViewSet)
router.register(r'categories',views.CategoryViewSet)

urlpatterns = [
    path('',include(router.urls))
]
