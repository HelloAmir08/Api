from django.urls import path
from example import views
from example.views import CategoryDetail, ProductDetail, ImageList, ImageDetail, CommentList, CommentDetail

urlpatterns = [
    path('category-list/', views.CategoryList.as_view(), name='category-list'),
    path('category-detail/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('product-list/', views.ProductList.as_view(), name='product-list'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('image-list/', ImageList.as_view(), name='image-list'),
    path('image-detail/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('comment-list/', CommentList.as_view(), name='comment-list'),
    path('comment-detail/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]