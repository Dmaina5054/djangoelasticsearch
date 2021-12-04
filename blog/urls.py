from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog.views import UserViewSet,ArticleViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'article',ArticleViewSet)

app_name = 'blog'
urlpatterns = [
    path('', include(router.urls)),
]
