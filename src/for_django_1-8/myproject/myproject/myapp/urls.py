# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list1'),
    url(r'^admin/',include(admin.site.urls)),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
