#coding:utf-8
from RedAnt.forms import teamForm,myUEditorModelForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from RedAnt.models import ProjectTeam,Blog,LearningResources
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required
import DUSite
from bs4 import BeautifulSoup
import urllib.request
import json
import re
import datetime
import random

@permission_required('RedAnt.add_ProjectTeam')
@login_required
def teamAdd(request):
    name = '未命名'
    introduction = '请添加项目简介'
    team = ProjectTeam.objects.create(TeamName=name,Introduction=introduction)
    team.save()
    form = myUEditorModelForm()
    url = '/teams/major='+ str(team.id) + '/edit/'
    return HttpResponseRedirect(url)

@login_required
def teamMajor(request,name):
    try:
        team = ProjectTeam.objects.get(ShortName=name)
    except:
        return HttpResponse(u"项目组不存在")
    if request.method == 'POST':
        form = myUEditorModelForm(request.POST)
        if form.is_valid():
            blog = form.save()
            blog.Team = team
            blog = transform(blog)
            blog.save()
            form = myUEditorModelForm()
            blogs = Blog.objects.filter(Team=team).order_by("-modify_time")
            teams = ProjectTeam.objects.all()
            return render(request, 'projectTeam.html', {'team': team, 'teams': teams,'form': form, 'blogs': blogs})
        else:
            return HttpResponse(u"数据校验错误")
    else:
        try:
            blogs = Blog.objects.filter(Team=team).order_by('-modify_time')
        except:
            blogs = ''
        form = myUEditorModelForm()
        teams = ProjectTeam.objects.all()
        return render(request, 'projectTeam.html', {'team': team,'teams': teams, 'form': form, 'blogs': blogs})

@login_required
def edit(request,name):
    if request.method == 'POST':
        form = teamForm(request.POST)
        if form.is_valid():
            try:
                ProjectTeam.objects.get(ShortName=name).delete()
            except:
                ProjectTeam.objects.get(id=int(name)).delete()
            team = form.save()
            url = '/teams/major=' + team.ShortName + '/'
            return HttpResponseRedirect(url)
        else:
            return HttpResponse(u"数据校验错误")
    else:
        try:
            team = ProjectTeam.objects.get(ShortName=name)
        except:
            team = ProjectTeam.objects.get(id=int(name))
        editor = teamForm(instance=team)
        teams = ProjectTeam.objects.all()
        return render(request, 'teamEdit.html', {'team': team,'teams': teams, 'editor': editor})

@permission_required('RedAnt.change_blog')
@login_required
def editBlog(request, name, article):

    if request.method == 'POST':
        form = myUEditorModelForm(request.POST)
        Blog.objects.get(Name=article).delete()
        if form.is_valid():
            blog = form.save()
            blog = transform(blog)
            blog.save()
            url = '/teams/major=' + name + '/ article = '+ article + '/'
            return HttpResponseRedirect(url)
        else:
            return HttpResponse(u"数据校验错误")
    else:
        article = Blog.objects.get(Name=article)
        form = myUEditorModelForm(instance=article)
        teams = ProjectTeam.objects.all()
        return render(request, 'editBlog.html', {'form': form,'teams': teams})

@permission_required('RedAnt.delete_blog')
@login_required
def deleteBlog(request, name, article):
    Blog.objects.get(Name=article).delete()
    url = '/teams/major=' + name + '/ '
    return HttpResponseRedirect(url)

def transform(blog):
    try:
        key = blog.Content
        soup = BeautifulSoup(key, "html5lib")
        blog.ImagePath = soup.img.get('src')
    except:
        blog.ImagePath = '/static/images/LOGO1.png'
    return blog
