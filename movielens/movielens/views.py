from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    pages = ['movies', 'raters', 'top']
    context = {'pages': pages}
    return render(request, 'home.html', context)
