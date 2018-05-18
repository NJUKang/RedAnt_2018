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
    if name == 'cptNw':
        teams = ProjectTeam.objects.all()
        return render(request, 'cptNw.html', {'teams': teams})
    if name == 'cptCp':
        teams = ProjectTeam.objects.all()
        return render(request, 'cptCp.html', {'teams': teams})
