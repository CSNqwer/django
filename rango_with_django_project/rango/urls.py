from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^index/about/$',views.about,name='about'),
    url(r'^index/category/(?P<category_name_slug>[\w\-]+)/$',views.category,name='category')
]