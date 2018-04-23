
from django.conf.urls import include, url
import RedAnt.courses.views as views

urlpatterns = [
    #url(r'major=(?P<name>.*)/edit', views.edit),
    url(r'major=(?P<name>.*)/', views.courseMajor),
    url(r'operating=new/', views.courseAdd),
    ]