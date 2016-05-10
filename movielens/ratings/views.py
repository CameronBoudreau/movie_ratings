from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie, Rater, Rating


def home(request):
    pages = ['movies', 'raters', 'top']
    context = {'is_authenticated': request.user.is_authenticated(),
               'pages': pages}
    return render(request, 'ratings/home.html', context)


def movie_index(request):
    search = False
    all_movies = Movie.objects.all().order_by('title')
    movie_cols = ['Title', 'Average Rating', 'URL']
    context = {'all_movies': all_movies, 'columns': movie_cols,
               'is_authenticated': request.user.is_authenticated()}
    if 'q' in request.GET and request.GET['q']:
        search = True
        q = request.GET['q']
        movies = Movie.objects.filter(title__icontains=q)
        message = 'You searched for: %r' % request.GET['q']
        context = {'message': message, 'query': q,
                   'movies': movies.order_by('title'),
                   'all_movies': all_movies.order_by('title'),
                   'columns': movie_cols,
                   'is_authenticated': request.user.is_authenticated(),
                   'search': search}
    return render(request, 'ratings/movie_index.html', context)


def rater_index(request):
    raters = Rater.objects.all()
    context = {'is_authenticated': request.user.is_authenticated(),
               'raters': raters, 'columns': ['ID', 'Age', 'Sex',
                                             'Occupation', 'Movies Rated']}
    return render(request, 'ratings/rater_index.html', context)


def top_rated(request):
    top_rated = Movie.get_top()
    movie_cols = ['Rank', 'Title', 'Average Rating',
                  'Total Ratings', 'URL']
    context = {'is_authenticated': request.user.is_authenticated(),
               'top_rated': top_rated, 'columns': movie_cols}
    return render(request, 'ratings/top_rated.html', context)


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
