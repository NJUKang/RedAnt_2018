#coding:utf-8
from RedAnt.forms import teamForm,myUEditorModelForm,FileUploadForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from RedAnt import models as m
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
from pprint import pprint
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
def courseMajor(request, name):
    teams = ProjectTeam.objects.all()
    zjs = m.ZhangJie.objects.filter(kecheng=name)
    context = {
        'teams': teams,
        'zjs': zjs,
        'kecheng': name,
    }
    if request.GET.get('zjs_id', None):
        zjsmall = m.ZhangJieSmall.objects.get(id=request.GET['zjs_id'])
        if request.GET.get('del', None):
            zjsmall.pics.all().delete()
            zjsmall.delete()
            return HttpResponseRedirect('/courses/major=%s/' % name)
        context['zjsmall'] = zjsmall
        context['zj'] = m.ZhangJieSmall.objects.get(id=request.GET['zjs_id']).zhangjie_set.all()[0]
    elif zjs.exists() and zjs[0].details.exists():
        context['zjsmall'] = zjs[0].details.all()[0]
        context['zj'] = zjs[0]
    return render(request, 'course_detail.html', context=context)


@login_required
def zhangjie_add(req):
    teams = ProjectTeam.objects.all()
    if req.method == 'GET':
        zjs = m.ZhangJie.objects.filter(kecheng=req.GET['kecheng'])
        return render(req, 'course_zhangjie_add.html',{
            'teams': teams,
            'zjs': zjs,
            'kecheng': req.GET['kecheng'],
        })
    zj, created = m.ZhangJie.objects.get_or_create(
        kecheng=req.POST['kecheng'],
        name=req.POST['name'],
    )
    return HttpResponseRedirect('/courses/major=%s/' % req.POST['kecheng'])


@login_required
def zhangjie_small_add(req):
    teams = ProjectTeam.objects.all()
    if req.method == 'GET':
        kecheng = req.GET['kecheng']
        zjs = m.ZhangJie.objects.filter(kecheng=kecheng)
        return render(req, 'course_zhangjie_small_add.html',{
            'teams': teams,
            'zjs': zjs,
            'zj': req.GET['zj'],
            'kecheng': kecheng,
            'zjs_id': req.GET.get('zjs_id', ''),
            'zjsmall': m.ZhangJieSmall.objects.get(
                id=req.GET['zjs_id']) if req.GET.get('zjs_id', '') else '',
            'type_': req.GET.get('type', ''),
        })

    zj = m.ZhangJie.objects.get(name=req.POST['zj'])

    zjsp_s = []
    pics = req.FILES.getlist('pics', [])
    for f in pics:
        fname = m.ZhangJieSmallPic.save_file(f)
        zjsp = m.ZhangJieSmallPic()
        zjsp.file = fname
        zjsp.save()
        zjsp_s.append(zjsp)
    if req.POST.get('zjs_id', None):
        zjs = m.ZhangJieSmall.objects.get(id=req.POST['zjs_id'])
    else:
        zjs = m.ZhangJieSmall()
        zjs.name = req.POST['name']
    if req.FILES.get('video', None):
        zjs.video = m.ZhangJieSmallPic.save_file(req.FILES['video'])
    if req.POST.get('video_desc', None):
        zjs.video_desc = req.POST['video_desc']
    if req.POST.get('content', None):
        zjs.content = req.POST['content']
    zjs.save()

    if pics:
        zjs.pics.all().delete()
        zjs.pics.add(*zjsp_s)

    zj.details.add(zjs)
    return HttpResponseRedirect('/courses/major=%s/?zjs_id=%s' % (req.POST['kecheng'],zjs.id))
