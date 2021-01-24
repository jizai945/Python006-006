from django.urls import path, re_path, register_converter
from . import views

urlpatterns=[
    path('index', views.comment),
    path('index/test', views.test),
]
