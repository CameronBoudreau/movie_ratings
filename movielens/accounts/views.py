from django.shortcuts import render
from django.http import HttpResponseRedirect


def profile(request):
    context = {'is_authenticated': request.user.is_authenticated(),
               'username': request.user.username
               }

    return render(request, 'accounts/profile.html', context)


def logout_success(request):
    return render(request, 'accounts/logout_success.html')


def create_user(request):
    context = {'form': RegisterForm()}
    return render(request, 'accounts/create_user.html', context)
