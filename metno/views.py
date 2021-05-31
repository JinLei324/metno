from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    
    context = {
        'a': 'sample',
    }
    return render(request, 'index.html', context)