from django.shortcuts import render, get_object_or_404
from .models import Movie, Rater, Rating


def home(request):
    pages = ['movies', 'raters', 'top']
    context = {'is_authenticated': request.user.is_authenticated(), 'pages': pages}
    return render(request, 'ratings/home.html', context)


def index(request, name):
    movies = Movie.objects.all().order_by('title')

    raters = Rater.objects.all()

    top_rated = Movie.get_top()

    if name == 'movies':
        movie_cols = ['Title', 'Average Rating', 'URL']
        context = {'movies': movies, 'columns': movie_cols,
                   'is_authenticated': request.user.is_authenticated()}
        return render(request, 'ratings/movie_index.html', context)

    elif name == 'raters':
        context = {'is_authenticated': request.user.is_authenticated(),
                   'raters': raters, 'columns': ['ID', 'Age', 'Sex',
                                                 'Occupation', 'Movies Rated']}
        return render(request, 'ratings/rater_index.html', context)

    elif name == 'top':
        rank = 1
        movie_cols = ['Rank', 'Title', 'Average Rating',
                      'Total Ratings', 'URL']
        context = {'is_authenticated': request.user.is_authenticated(),
                   'top_rated': top_rated, 'columns': movie_cols, 'rank': rank}
        return render(request, 'ratings/top_rated.html', context)

    else:
        return render(request, 'ratings/redirect.html')


def movie_detail(request, movie):
    movie = get_object_or_404(Movie, id=movie)
    ratings = Rating.objects.filter(movie_id=movie)
    context = {'is_authenticated': request.user.is_authenticated(),
               'movie': movie, 'ratings': ratings}
    return render(request, 'ratings/movie_detail.html', context)


def rater_detail(request, rater):
    rater = get_object_or_404(Rater, id=rater)
    ratings = Rating.objects.filter(rater_id=rater)
    context = {'is_authenticated': request.user.is_authenticated(),
               'rater': rater, 'ratings': ratings}
    return render(request, 'ratings/rater_detail.html', context)


def new(request, rater):
    pass
