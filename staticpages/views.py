from django.shortcuts import render

# Create your views here.
import os


def index(request):
    # settings.py
    TEST = os.getenv("TESTABC")
    context = {'test': TEST
    }
    return render(request, 'staticpages/index.html', context)


def dashboard(request):
    # settings.py
    TEST = os.getenv("TESTABC")
    context = {'test': TEST
    }
    return render(request, 'staticpages/dashboard.html', context)

def login(request):
    context = {
    }
    return render(request, 'staticpages/login.html', context)

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

    mytable = {}
    
    context = { 'mytable': mytable
    }
    return render(request, 'staticpages/tables.html', context)