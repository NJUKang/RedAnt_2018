#coding:utf-8
from RedAnt.forms import myUEditorModelForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from RedAnt.models import Blog
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
        return render(request, 'signIn.html')

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
    return render(request, 'home.html',{'name':request.user.username})

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
        return render(request, 'personalCenter.html')

@login_required
def webTeam(request):
    if request.method == 'POST':
        form = myUEditorModelForm(request.POST)
        if form.is_valid():
            # if(Blog.objects.filter(Name='form.Meta.model.Name')):
            # Blog.objects.filter(Name='form.Meta.model.Name').update(form.Meta.model)
            form.save()
            form = myUEditorModelForm()
            blogs = Blog.objects.all().order_by("-modify_time")
            return render(request,'webTeam.html', {'name':request.user.username, 'form': form, 'blogs': transform(blogs)})
        else:
            return HttpResponse(u"数据校验错误")
    else:
        form = myUEditorModelForm()
        blogs = Blog.objects.all().order_by('-modify_time')
        return render(request, 'webTeam.html', {'name':request.user.username, 'form': form, 'blogs': transform(blogs)})

@login_required
def readmore(request,name):
    article = Blog.objects.get(Name=name)
    article.Description = article.Name
    key = article.Name
    soup = BeautifulSoup(key, "html5lib")
    article.Name = soup.get_text()
    return render(request, 'article.html',{'name':request.user.username, 'article': article})

@permission_required('RedAnt.change_blog')
@login_required
def edit_blog(request,name):
    article = Blog.objects.get(Name=name)
    if request.method == 'POST':
        form = myUEditorModelForm(request.POST)
        Blog.objects.get(Name=name).delete()
        if form.is_valid():
            # if(Blog.objects.filter(Name='form.Meta.model.Name')):
            # Blog.objects.filter(Name='form.Meta.model.Name').update(form.Meta.model)
            form.save()
            article = form.instance
            article.Description = article.Name
            key = article.Name
            soup = BeautifulSoup(key, "html5lib")
            article.Name = soup.get_text()
            return render(request,'article.html', {'name':request.user.username, 'article': article})
        else:
            return HttpResponse(u"数据校验错误")
    else:
        form = myUEditorModelForm(instance=article)
        return render(request, 'editBlog.html', {'name':request.user.username, 'form': form})

@login_required
def course(request):
    return render(request,'course.html',{'name':request.user.username})

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
                    group = Group.objects.get(name='Admin')
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
        return render(request, 'manager.html',{'users':users})

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
                    group = Group.objects.get(name='Admin')
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
        users = User.objects.filter(groups__name='Admin')
        return render(request, 'powerUserManage.html',{'users':users})

def transform(blogs):
    for blog in blogs:
        blog.Content = blog.Name
        key = blog.Name
        soup = BeautifulSoup(key, "html5lib")
        blog.Name = soup.get_text()
        try:
            key = blog.ImagePath
            soup = BeautifulSoup(key, "html5lib")
            blog.ImagePath = soup.img.get('src')
        except:
            blog.ImagePath = '/static/images/LOGO1.png'
        key = blog.Description
        soup = BeautifulSoup(key, "html5lib")
        blog.Description = soup.get_text()[:50]+'……'
    return blogs
