# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Destination
from django.shortcuts import render

def index(request):

    dests = Destination.objects.all()
    
    return render(request,"index.html",{'dests':dests})

def destinations(request):
    return render(request,"destinations.html")

def contact(request):
    return render(request,"contact.html")

def elements(request):
    return render(request,"elements.html")