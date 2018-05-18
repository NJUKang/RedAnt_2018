from django.conf.urls import include, url
import RedAnt.forum.views as views

urlpatterns = [
    url(r'', views.index),
    url(r'forum=(?P<name>.*)/',views.forum)
]