#coding:utf-8
from RedAnt.forms import myUEditorModelForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from RedAnt.models import Blog
import DUSite
from bs4 import BeautifulSoup
import urllib.request
import re

def index(request):
    return render_to_response('index.html')

def webTeam(request):
    if request.method == 'POST':
        form = myUEditorModelForm(request.POST)
        if form.is_valid():
            # if(Blog.objects.filter(Name='form.Meta.model.Name')):
            # Blog.objects.filter(Name='form.Meta.model.Name').update(form.Meta.model)
            form.save()
            form = myUEditorModelForm()
            blogs = Blog.objects.all().order_by("-modify_time")
            return render_to_response('WebTeam/WebTeam.html', {'form': form, 'blogs': transform(blogs)})
        else:
            return HttpResponse(u"数据校验错误")
    else:
        form = myUEditorModelForm()
        blogs = Blog.objects.all().order_by('-modify_time')
        return render_to_response('WebTeam/WebTeam.html', {'form': form, 'blogs': transform(blogs)})

def readmore(request,name):
    article = Blog.objects.get(Name=name)
    key = article.ImagePath
    soup = BeautifulSoup(key, "html5lib")
    article.ImagePath = soup.img.get('src')
    return render_to_response('WebTeam/readmore.html',{'article': article})

def transform(blogs):
    for blog in blogs:
        key = blog.ImagePath
        soup = BeautifulSoup(key, "html5lib")
        blog.ImagePath = soup.img.get('src')
        key = blog.Description
        soup = BeautifulSoup(key, "html5lib")
        blog.Description = soup.get_text()
    return blogs
