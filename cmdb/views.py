# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # request.POST
    # request.GET
    return render(request,"index.html")

