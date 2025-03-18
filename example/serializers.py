from rest_framework import serializers
from example.models import Category, Product, Image, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'






