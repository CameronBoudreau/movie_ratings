from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie, Rater, Rating


def index(request, name):
    movies = Movie.objects.all().order_by('title')
    movie_cols = ['Title', 'Release Date', 'Average Rating', 'Total Ratings',
                  'URL']
    top_rated = Movie.get_top()
    if name == 'movies':
        context = {'movies': movies, 'columns': movie_cols}
        return render(request, 'ratings/movies_index.html', context)
    elif name == 'raters':
        pass
    elif name == 'top':
        movie_cols = ['Average Rating', 'Title', 'Release Date', 'Total Ratings', 'URL']
        context = {'top_rated': top_rated, 'columns': movie_cols}
        return render(request, 'ratings/top_rated.html', context)
    else:
        return render(request, 'ratings/redirect.html')


def movie_index(request):
    return HttpResponse("""For now, enter a movie ID after '.../movies/' in your
                        browser to find movie info.""")


def movie_detail(request, movie):
    return HttpResponse("You're looking at the movie details for %s." % movie)


def rater_index(request):
    return HttpResponse("""For now, enter a movie ID after '.../raters/' in your
                        browser to find rater info.""")


def rater_detail(request, rater):
    return HttpResponse("You're looking at the rater details for rater #%s."
                        % rater)


def top_detail(request):
    return HttpResponse("This will display the top movies.")
