
from django.urls import path, include
from .views import ProductViewset
from rest_framework import  routers



router = routers.DefaultRouter()
router.register(r'products',ProductViewset,basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
