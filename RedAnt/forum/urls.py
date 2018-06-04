from django.conf.urls import include, url
import RedAnt.forum.views as views

urlpatterns = [
    url(r'post/', views.post),
    url(r'forum=(?P<name>.*)/page=(?P<page>[0-9]+)/delete=(?P<post>[0-9]+)/',views.deleteLpost),
    url(r'forum=(?P<name>.*)/page=(?P<page>[0-9]+)/delete/',views.delete),
    url(r'forum=(?P<name>.*)/page=(?P<page>[0-9]+)/',views.forum),
    url(r'forum=(?P<name>.*)/',views.forumJump),
    url(r'', views.index),
]