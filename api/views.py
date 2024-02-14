
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer