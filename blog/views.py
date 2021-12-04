from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import  viewsets

from blog.models import Category,Article
from blog.serializers import CategorySerializer,ArticleSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = UserSerializer
    queryset = User.objects.all() 
    
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    model = Article
    queryset = Article.objects.all()

