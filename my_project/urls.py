'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-03-16 13:55:39
LastEditors: TianyuYuan
LastEditTime: 2021-03-18 17:58:20
'''
"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from boards import views
from accounts import views as accounts_views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^signup/$',accounts_views.signup, name='signup'),
    re_path(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics,name="board_topics"),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name="new_topic"),
    re_path(r'^admin/', admin.site.urls),
]
