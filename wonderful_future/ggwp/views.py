# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from ggwp.models import Category,Page
from ggwp.forms import CategoryForm,PagesForm,UserProfileForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from ggwp.bing_search import run_query
from django.shortcuts import redirect

# Create your views here.
@login_required
def restricted(request):
    return render(request,'ggwp/restricted.html',)

"""def index(request):
    request.session.set_test_cookie()
    context = Category.objects.order_by('-likes')[:5]
    visits = int(request.COOKIES.get('visits','1'))
    reset_last_visit_time = False
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7],'%Y-%m-%d %H:%M:%S')
        if (datetime.now()-last_visit_time).days >1:
            visits = visits + 1
            reset_last_visit_time = True
        response = render(request, 'ggwp/index.html', {'categories': context, 'visits': visits})
    else:
        reset_last_visit_time = True
        response = render(request,'ggwp/index.html',{'categories':context,'visits':visits})
    if reset_last_visit_time:
        response.set_cookie('last_visit',datetime.now())
        response.set_cookie('visits',visits)
    return response"""

def index(request):
    context = Category.objects.order_by('-likes')[:6]
    page_list = Page.objects.order_by('-views')[:5]
    visits = request.session.get('visits')
    if not visits:
        visits =1
    reset_last_visit_time = False
    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7],'%Y-%m-%d %H:%M:%S')
        if (datetime.now()-last_visit_time).seconds > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True
    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    return render(request,'ggwp/index.html',{'categories':context,'visits':visits,'pages':page_list})

def about(request):
    context_dict1 = {'aboutmessage':'Range says: Hello world!!'}
    return render(request,'ggwp/about.html',context_dict1)

def category(request,mulu_name):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)
            context_dict['result_list'] = result_list
            context_dict['query'] = query
    try:
        category = Category.objects.get(slug=mulu_name)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category).order_by('-views')
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    if not context_dict['query']:
        context_dict['query'] = category.name
    return render(request,'ggwp/category.html',context_dict)
@login_required
def add_category(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request,'ggwp/add_category.html',{'form':form})
@login_required
def add_page(request,mulu_name):
    try:
        cat = Category.objects.get(slug=mulu_name)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PagesForm(request.POST)
        if form.is_valid():
            if cat:
                print(form.cleaned_data)
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request,mulu_name)
        else:
            print form.errors
    else:
        form = PagesForm()
    context_dict = {'form':form ,'category':cat}
    return render(request,'ggwp/add_page.html',context_dict)

def register(request):
    if request.session.test_cookie_worked():
        print '>>>>TEST COOKIE WORKED!'
        request.session.delete_test_cookie()
    registers = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileForm(data=request.POST)
        if user_form.is_valid() and user_profile.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_profile.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registers = True
        else:
            print user_form.errors,user_profile.errors
    else:
        user_form = UserForm()
        user_profile = UserProfileForm()
    return render(request,'ggwp/register.html',{'user_form':user_form,'user_profile':user_profile,'registers':registers})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/ggwp/index/')
            else:
                return HttpResponse('Your Ggwp account is disabled.')

        else:
            print 'Invalid login detail:{0},{1}'.format(username,password)
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request,'ggwp/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/ggwp/index/')

def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'ggwp/search.html', {'result_list': result_list})

def track_url(request):
    page_id = None
    url = '/ggwp/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass
    return redirect(url)



