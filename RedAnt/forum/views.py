from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
import urllib.request
from RedAnt.forms import postForm,myUEditorModelForm
from RedAnt.models import Post,lPost,ProjectTeam,Course
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.all().order_by('-modify_time')
    teams = ProjectTeam.objects.all()
    courses = Course.objects.all()
    return render(request, 'forum.html',{'teams': teams,'posts':posts,'courses': courses})

def post(request):
    if request.method == 'POST':
        form = myUEditorModelForm(request.POST)
        if form.is_valid():
            lpost = lPost()
            post = Post()
            blog = form.save()
            lpost.Content = blog.Content
            post.postedBy = request.user
            post.name = blog.Name
            post.postNum = 1
            lpost.postedBy = request.user
            post.save()
            lpost.post = post
            lpost.save()
            blog.delete()
            url = '/forum/'
            return HttpResponseRedirect(url)
    else:
        form = myUEditorModelForm()
        teams = ProjectTeam.objects.all()
        courses = Course.objects.all()
        return render(request,'forums.html',{'teams': teams,'form': form,'courses': courses})

def forum(request,name,page):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            temp = form.save()
            lpost = temp
            lpost.post = Post.objects.get(id = name)
            lpost.post.postNum = str(int(lpost.post.postNum) + 1)
            lpost.post.save()
            lpost.postedBy = request.user
            temp.delete()
            lpost.save()
        url = request.get_full_path()
        return HttpResponseRedirect(url)
    else:
        lposts = lPost.objects.filter(post_id=name).order_by('modify_time')
        lpost = lposts[0]
        lposts = lposts[1:]
        post = postForm()
        name = Post.objects.get(id=name).name
        teams = ProjectTeam.objects.all()
        courses = Course.objects.all()
        return render(request, 'forumContent.html',{'teams': teams,'lposts':lposts,'lpost':lpost,'post':post,'name':name,'courses': courses})

def forumJump(request,name):
    url = request.get_full_path()+'page=1/'
    return HttpResponseRedirect(url)

def deleteLpost(request,name,page,post):
    lPost.objects.get(id=post).delete()
    post =  Post.objects.get(id=name)
    post.postNum = str(int(post.postNum) - 1)
    post.save()
    url = '/forum/forum='+name+'/'
    return HttpResponseRedirect(url)

def delete(request,name,page):
    Post.objects.get(id=name).delete()
    url = '/forum/'
    return HttpResponseRedirect(url)