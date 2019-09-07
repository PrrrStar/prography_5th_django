
"""
crudapp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.post_list, name='post_list'),
    path(r'^detail/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    path(r'^add', views.post_add, name='post_add'),
    path(r'^edit/(?P<pk>\d+)$', views.post_edit, name='post_edit'),
    path(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),

]