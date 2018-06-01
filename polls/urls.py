# -*- coding: utf-8 -*-
"""
Created on 2018/6/1

@author: xing yan
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]