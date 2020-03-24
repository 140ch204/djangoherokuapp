from django.http import HttpResponseRedirect

from django.shortcuts import render

from .forms import NameForm

from .apidatagouv import *

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


def login2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    context = {'form': form}

    return render(request, 'staticpages/login.html', context)




def testapi(request):

    mydata = GouvApiData()

    mydata.search_active_by_cp('91790',0)

    total = mydata.total_results


    context = {'testapi': total }

    return render(request, 'staticpages/testapi.html', context)



def siret(request,siret):

    mydata = GouvApiData()

    data_entreprise = mydata.search_by_siret(siret).json()['etablissement']

    etablissement = {key:val for key, val in data_entreprise.items() if val is not None}

    unite_legale = {key:val for key, val in data_entreprise['unite_legale'].items() if val is not None}

    etablissement_siege = {key:val for key, val in data_entreprise['unite_legale']['etablissement_siege'].items() if val is not None}

    context = {'siret': siret, 
        'etablissement' : etablissement,
        'unite_legale' : unite_legale,
        'etablissement_siege' : etablissement_siege,
         }

    return render(request, 'staticpages/siret.html', context)