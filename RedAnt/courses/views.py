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
def courseAdd(request):
    name = '未命名'
    introduction = '请添加项目简介'
    team = ProjectTeam.objects.create(TeamName=name,Introduction=introduction)
    team.save()
    form = myUEditorModelForm()
    url = '/teams/major='+ str(team.id) + '/edit/'
    return HttpResponseRedirect(url)

@login_required
def courseMajor(request,name):
    # try:
    #     team = ProjectTeam.objects.get(ShortName=name)
    # except:
    #     return HttpResponse(u"项目组不存在")
    # if request.method == 'POST':
    #     form = myUEditorModelForm(request.POST)
    #     if form.is_valid():
    #         blog = form.save()
    #         blog.Team = team
    #         blog = transform(blog)
    #         blog.save()
    #         form = myUEditorModelForm()
    #         blogs = Blog.objects.filter(Team=team).order_by("-modify_time")
    #         return render(request, 'projectTeam.html', {'team': team, 'form': form, 'blogs': blogs})
    #     else:
    #         return HttpResponse(u"数据校验错误")
    # else:
    #     try:
    #         blogs = Blog.objects.filter(Team=team).order_by('-modify_time')
    #     except:
    #         blogs = ''
    #     form = myUEditorModelForm()
    #     return render(request, 'projectTeam.html', {'team': team, 'form': form, 'blogs': blogs})
    if name == 'cptNw':
        teams = ProjectTeam.objects.all()
        return render(request, 'cptNw.html', {'teams': teams})
    if name == 'cptCp':
        teams = ProjectTeam.objects.all()
        return render(request, 'cptCp.html', {'teams': teams})
