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

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get("email", False)
        password = request.POST.get("password", False)
        try:
            user = User.objects.get(email = email)
            username = user.username
            # 获取的表单数据与数据库进行比较
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # 登录成功
                    login(request, user)  # 登录用户
                    data = {'code': '1', 'info': u'登录成功', 'url': 'index'}
                else:
                    data = {'code': '0', 'info': u'用户未激活'}
            else:
                data = {'code': '0', 'info': u'邮箱或密码错误'}

            return JsonResponse(data)
        except:
            data = {'code': '0', 'info': u'邮箱或密码错误'}
            return JsonResponse(data)
    else:
        teams = ProjectTeam.objects.all()
        return render(request, 'signIn.html',{'teams':teams})

def logout_system(request):
    """
    退出登录
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect('/index/sign_in/')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            data = {'code': '0', 'info': u'用户名冲突'}
            return JsonResponse(data)
        except :
            try:
                User.objects.get(email=email)
                data = {'code': '0', 'info': u'邮箱已注册'}
                return JsonResponse(data)
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, email=email, password=password)
                if user is not None:
                    # user.is_active = False
                    first_name = datetime.datetime.now().strftime('%Y%m%d')+str(random.randint(100,999))
                    user.first_name = first_name
                    group = Group.objects.get(name='ordUser')
                    user.groups.add(group)
                    user.save()
                    login(request, user)
                    data = {'code': '1', 'info': u'注册成功'}
                    return JsonResponse(data)
    else:
        return render(request,'signUp.html')

@login_required
def index(request):
    teams = ProjectTeam.objects.all()
    return render(request, 'home.html',{'teams':teams})