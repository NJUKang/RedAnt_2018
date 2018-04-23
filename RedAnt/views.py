#coding:utf-8
from RedAnt.forms import myUEditorModelForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from RedAnt.models import Blog,ProjectTeam
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

@login_required
def account_manager(request):
    if request.method == 'POST':
        username = request.POST.get("username", False)
        email = request.POST['email']
        password = request.POST['password']
        project = request.POST.get("project", False)
        print(project)
        try:
            user = User.objects.get(username=username)
            if(request.user == user):
                raise
            data = {'code': '0', 'info': u'用户名冲突'}
            return JsonResponse(data)
        except:
            try:
                user = User.objects.get(email=email)
                if (request.user == user):
                    raise
                data = {'code': '0', 'info': u'邮箱已注册'}
                return JsonResponse(data)
            except User.DoesNotExist:
                if(username.strip() !=''):
                    request.user.username = username
                if (email.strip() != ''):
                    request.user.email = email
                if (password.strip() != ''):
                    request.user.set_password(password)
                request.user.save()
                data = {'code': '1', 'info': u'修改成功'}
                return JsonResponse(data)
    else:
        teams = ProjectTeam.objects.all()
        return render(request, 'personalCenter.html', {'teams': teams})


@login_required
def course(request):
    teams = ProjectTeam.objects.all()
    return render(request,'course.html',{'name':request.user.username,'teams': teams})

@login_required
def manage(request):
    if request.method == 'POST':
        userlist = request.POST.get("userList")
        status = request.POST.get("status")
        names = re.findall(r"'username':'(.+?)'", userlist)
        try:
            if status == 'changeRank':
                for username in names:
                    user = User.objects.get(username=username)
                    group = Group.objects.get(name='ordUser')
                    user.groups.remove(group)
                    group = Group.objects.get(name='admin')
                    user.groups.add(group)
                data = {'code': '1', 'info': u'修改成功'}
            else:
                for username in names:
                    User.objects.get(username=username).delete()
                data = {'code': '1', 'info': u'删除成功'}
            return JsonResponse(data)
        except:
            data = {'code': '0', 'info': u'修改失败'}
            return JsonResponse(data)
    else:
        users = User.objects.filter(groups__name='ordUser')
        teams = ProjectTeam.objects.all()
        return render(request, 'manager.html',{'users':users, 'teams': teams})

@login_required
def vip_manage(request):
    if request.method == 'POST':
        userlist = request.POST.get("userList")
        status = request.POST.get("status")
        names = re.findall(r"'username':'(.+?)'", userlist)
        print(userlist)
        print(status)
        print(names)
        try:
            if status == 'changeRank':
                for username in names:
                    user = User.objects.get(username=username)
                    group = Group.objects.get(name='admin')
                    user.groups.remove(group)
                    group = Group.objects.get(name='ordUser')
                    user.groups.add(group)
                data = {'code': '1', 'info': u'修改成功'}
            else:
                for username in names:
                    User.objects.get(username=username).delete()
                data = {'code': '1', 'info': u'删除成功'}
            return JsonResponse(data)
        except:
            data = {'code': '0', 'info': u'修改失败'}
            return JsonResponse(data)
    else:
        users = User.objects.filter(groups__name='admin')
        teams = ProjectTeam.objects.all()
        return render(request, 'powerUserManage.html',{'users':users, 'teams': teams})
