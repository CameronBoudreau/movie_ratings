from djang import forms

from.models import Movie, Rater, ratings


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'release', 'url')
