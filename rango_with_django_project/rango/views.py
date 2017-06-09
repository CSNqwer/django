# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rango.models import  Category,Page
# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    return render(request,'rango/index.html',{'categroies':category_list})

#def about(request):
   # return HttpResponse("Rango says here is the about page.<br/><a href='/rango/index'>Index<a/>")# :

def about(request):
    context_dict1 = {'aboutmessage':'Range says: Hello world!!'}
    return render(request,'rango/about.html',context_dict1)

def category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request,'rango/category.html',context_dict)

