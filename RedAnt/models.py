#coding:utf-8
#
from django.db import models
from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import *
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from DUSite import settings
import os

class ProjectTeam(models.Model):
    TeamName = models.CharField(u'项目组名称',max_length=100,null = True)
    ShortName= models.CharField(u'英文缩写',max_length=100,null = True)
    Introduction = UEditorField(u'项目组简介',height=100, width=788, toolbars="mini")

class Blog(models.Model):
    Name = models.CharField(u'名称',max_length=100)
    ImagePath =  models.CharField(u'图片',max_length=20,null = True)
    # Description = models.CharField(u'概述', null = True)
    Content = UEditorField(u'内容', height=200, width='100%', imagePath="images/", filePath='files/',
                           toolbars="besttome")
    modify_time = models.DateTimeField(auto_now=True)
    Team = models.ForeignKey('ProjectTeam',null=True,on_delete=models.CASCADE,)

def get_upload_path(instance, filename):
    name = instance.teamName
    return 'Resourses/%s/%s' % (name,filename)


class LearningResources(models.Model):
    Team = models.ForeignKey('ProjectTeam',on_delete=models.CASCADE,)
    teamName = models.CharField(max_length=100,null = True)
    fileField = models.FileField(upload_to=get_upload_path)
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30, blank=True, null=True)

@receiver(post_delete, sender=LearningResources)
def delete_upload_files(sender, instance, **kwargs):
        files = getattr(instance, 'fileField', '')
        if not files:
            return
        fname = os.path.join(settings.MEDIA_ROOT, str(files))
        if os.path.isfile(fname):
            os.remove(fname)