from django.db import models
from django.db.models import SET_NULL, CASCADE
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name

class Image(BaseModel):
    product = models.ForeignKey(Product, on_delete=CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=CASCADE, blank=True, null=True, related_name='comments')
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


