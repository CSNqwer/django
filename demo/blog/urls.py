from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_article,name='edit_article'),
    url(r'^edit/action/$', views.action,name='action'),
]