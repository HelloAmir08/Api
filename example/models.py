from django.db import models
from django.db.models import SET_NULL


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
    image = models.ImageField(upload_to='products', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name

