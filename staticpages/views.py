from django.shortcuts import render

# Create your views here.
import os


def landing(request):
    # settings.py
    TEST = os.getenv("TESTABC")
    context = {'test': TEST
    }
    return render(request, 'staticpages/index.html', context)

def login(request):
    context = {
    }
    return render(request, 'staticpages/index.html', context)

def register(request):
    context = {
    }
    return render(request, 'staticpages/index.html', context)

def forgot(request):
    context = {
    }
    return render(request, 'staticpages/index.html', context)

def charts(request):
    context = {
    }
    return render(request, 'staticpages/index.html', context)

def tables(request):
    context = {
    }
    return render(request, 'staticpages/index.html', context)