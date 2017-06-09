# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','data')
    list_filter = ('data','title')
admin.site.register(Article,ArticleAdmin)
