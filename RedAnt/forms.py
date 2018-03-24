# coding:utf-8
from django import forms
from DjangoUeditor.widgets import UEditorWidget
from DjangoUeditor.forms import UEditorField, UEditorModelForm
from .models import Blog

class myUEditorModelForm(UEditorModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
