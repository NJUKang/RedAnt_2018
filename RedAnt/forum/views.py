from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
import urllib.request

def index(request):
    return render(request, 'forumContent.html')

def forum(request,name):
    return render(request, 'forum.html')