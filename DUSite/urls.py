#coding:utf-8
from . import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django import views
import RedAnt.views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'DUSite.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^index/$', RedAnt.views.index),
    url(r'^webTeam/$', RedAnt.views.webTeam),
    url(r'^webTeam/(?P<name>.*)$', RedAnt.views.readmore),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT }),
        url(r'^static/(?P<path>.*)$',views.static.serve,{'document_root':settings.STATIC_ROOT}),
        url(r'^(?P<path>.*)$',views.static.serve,{'document_root':settings.STATIC_ROOT}),
    ]