from django.urls import path
from example import views
from example.views import CategoryDetail, ProductDetail

urlpatterns = [
    path('category-list/', views.CategoryList.as_view(), name='category-list'),
    path('category-detail/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('product-list/', views.ProductList.as_view(), name='product-list'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]