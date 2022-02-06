from django.urls import path, include
from .views import blog_view, blog_about_view

urlpatterns = [
    path('',  blog_view),
    path('about',  blog_about_view),
]
