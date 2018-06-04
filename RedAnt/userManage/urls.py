from django.conf.urls import include, url
import RedAnt.userManage.views as views

urlpatterns = [
    url(r'changeGroup/', views.changeGroup),
    url(r'invitation/', views.invitation),
    url(r'powerUser/', views.vip_manage),
    url(r'', views.manage),
    ]