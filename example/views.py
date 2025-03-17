from django.shortcuts import render
from rest_framework import generics
from example.models import Category, Product
from example.serializers import CategorySerializer, ProductSerializer

'''Category views'''
#Category list + create
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Category detail + update, delete
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

'''Product views'''
#Product list + create
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#Product detail + update, delete
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

