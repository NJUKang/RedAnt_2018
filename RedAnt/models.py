#coding:utf-8
#
from django.db import models
from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import *

class ProjectTeam(models.Model):
    TeamName = models.CharField(u'项目组名称',max_length=100,null = True)
    ShortName= models.CharField(u'英文缩写',max_length=100,null = True)
    Introduction = UEditorField(u'项目组简介',height=100, width=788, toolbars="mini")

class Blog(models.Model):
    Name = models.CharField(u'名称',max_length=100,primary_key = True)
    ImagePath =  models.CharField(u'图片',max_length=20,null = True)
    # Description = models.CharField(u'概述', null = True)
    Content = UEditorField(u'内容', height=200, width='100%', imagePath="images/", filePath='files/',
                           toolbars="besttome")
    modify_time = models.DateTimeField(auto_now=True)
    Team = models.ForeignKey('ProjectTeam',null=True,on_delete=models.CASCADE,)

class LearningResources(models.Model):
    Name = models.CharField(max_length=20)
    Team = models.ForeignKey('ProjectTeam',on_delete=models.CASCADE,)
