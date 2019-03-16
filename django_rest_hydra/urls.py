# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'django_rest_hydra'
urlpatterns = [
    path('test/', views.TestView.as_view())
    ]
