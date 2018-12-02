from django.shortcuts import render
from .models import Post
'from django.http import HttpResponse'

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')

def about(request):

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/about.html', context)
