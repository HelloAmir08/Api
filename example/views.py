from django.shortcuts import render
from rest_framework import generics
from example.models import Category, Product, Image, Comment
from example.serializers import CategorySerializer, ProductSerializer, ImageSerializer, CommentSerializer
from example.permissions import OnlyWeekDays, CommentPermission

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

'''Image views'''
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

'''Comment views'''
class CommentList(generics.ListCreateAPIView):
    permission_classes = [OnlyWeekDays]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CommentPermission, OnlyWeekDays]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



