from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Burak Alp',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Augest 27, 2018',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Augest 28, 2018',
    }
]

def blog_view(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context)

def blog_about_view(request):
    return render(request, 'blog_about.html')

