#coding:utf-8
#
from django.db import models
from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import *

class Blog(models.Model):
    Name = models.CharField(u'日志标题', max_length=100, primary_key = True)
    ImagePath = UEditorField(u'封面图片', height=100, width=300, toolbars="supermini",imagePath="images/")
    Description = UEditorField(u'描述', height=50, width=621, toolbars="mini")
    Content = UEditorField(u'内容', height=200, width=621, imagePath="images/", filePath='files/',
                           toolbars="besttome")
    modify_time = models.DateTimeField(auto_now=True)




