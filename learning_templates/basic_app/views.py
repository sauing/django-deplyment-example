# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
def index(request):
    context_dict = {'text': "hello world", 'number':100}
    return render(request,'basic_app/index.html',context_dict)
# Create your views here.

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
