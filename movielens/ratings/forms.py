from django import forms


class SearchForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'release', 'url')
