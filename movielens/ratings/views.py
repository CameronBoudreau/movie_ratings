from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ratings index.")


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
