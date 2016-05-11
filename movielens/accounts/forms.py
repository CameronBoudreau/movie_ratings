from ratings.models import Rater, User
from django import forms


class RaterForm(forms.ModelForm):
    age = forms.IntegerField()
    sex = forms.CharField(max_length=1)

    class Meta:
        model = Rater
        exclude = ['user', 'avg_rating', 'total_ratings']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username',  'password', 'first_name', 'last_name', 'email')
