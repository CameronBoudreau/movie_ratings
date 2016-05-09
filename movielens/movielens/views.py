from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    pages = ['movies', 'raters', 'top']
    context = {'pages': pages, 'is_authenticated': request.user.is_authenticated()}
    return render(request, 'home.html', context)
