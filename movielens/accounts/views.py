from django.shortcuts import render, render_to_response
from .forms import RaterForm, UserForm
from django.template import RequestContext


def profile(request):
    context = {'is_authenticated': request.user.is_authenticated(),
               'username': request.user.username
               }

    return render(request, 'accounts/profile.html', context)


def logout_success(request):
    return render(request, 'accounts/logout_success.html')


def register(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='user')
        rater_form = RaterForm(request.POST, prefix='rater')

        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save()
            rater = rater_form.save(commit=False)
            rater.user = user
            rater.save()
            # user.save()

            return render(request, 'accounts/profile')
    else:
        user_form = UserForm(prefix='user')
        rater_form = RaterForm(prefix='rater')

    return render_to_response(
            'registration/register.html',
            {'rater_form': rater_form,
             'user_form': user_form},
            context_instance=RequestContext(request))
