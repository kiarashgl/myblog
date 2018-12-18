from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def index(request):
    return render(request,'index.html',{'posts' : Post.objects.all()})