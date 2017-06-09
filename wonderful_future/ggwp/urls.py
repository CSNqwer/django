from django.conf.urls import url
from django.contrib import admin
from ggwp import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^add_category/$',views.add_category,name='add_category'),
    url(r'^category/(?P<mulu_name>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
    url(r'^category/(?P<mulu_name>[\w\-]+)/$',views.category,name='category'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^about/$',views.about,name='about'),
    url(r'^restricted/',views.restricted,name='restricted'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^search/$',views.search,name='search'),
    url(r'^goto/$',views.track_url,name="goto"),
]