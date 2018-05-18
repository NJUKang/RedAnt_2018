# coding:utf-8
from django import forms
from DjangoUeditor.widgets import UEditorWidget
from DjangoUeditor.forms import UEditorField, UEditorModelForm
from .models import Blog,ProjectTeam

class teamForm(UEditorModelForm):
    class Meta:
        model = ProjectTeam
        fields = ('TeamName', 'ShortName', 'Introduction')
        widgets = {
            "TeamName": forms.TextInput(attrs={"style": "width:788px;" }),
            "ShortName": forms.TextInput(attrs={"style": "width:788px;" }),
            # 直接设置style或者某项属性改变样式，记得字典格式，赋值给attrs
        }

class myUEditorModelForm(UEditorModelForm):
    class Meta:
        model = Blog
        fields = ('Name', 'Content')
        widgets = {
            "Name": forms.TextInput(attrs={"style": "width:100%;"}),
        # 直接设置style或者某项属性改变样式，记得字典格式，赋值给attrs
        }

class FileUploadForm(forms.Form):
    file = forms.FileField()