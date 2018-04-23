
from django.conf.urls import include, url
import RedAnt.index.views as views

urlpatterns = [
    url(r'sign_in/', views.sign_in),
    url(r'sign_up/', views.sign_up),
    url(r'logout/', views.logout_system),
    url(r'', views.index),
    ]