# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Homepage<h1>')
