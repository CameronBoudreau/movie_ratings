from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release = models.DateField()
    url = models.CharField(max_length=200, default="N/A")
    avg_rating = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    total_ratings = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_average(self):
        return Rating.objects.filter(movie_id=self.id).aggregate(Avg('score'))

    def get_total(self):
        return Rating.objects.filter(movie_id=self.id).aggregate(Count('score'))

    @staticmethod
    def get_top(num=20):
        ratings_list = []
        for movie in Movie.objects.all():
            if movie.total_ratings > 100:
                ratings_list.append((movie.id, movie.avg_rating))
        ratings_list = sorted(ratings_list, key=lambda movie: movie[1],
                              reverse=True)
        top_rated = []
        for i in ratings_list:
            top_rated.append(Movie.objects.get(id=i[0]))
        return top_rated[:num]


class Rater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=200, default="-")
    occupation = models.CharField(max_length=200, default="Not given")
    avg_rating = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    total_ratings = models.IntegerField(default=0)

    def __str__(self):
        return ("{}: {} {} {}".format(self.id, self.age, self.sex,
                                      self.occupation))

    def get_average_rating(self):
        return Rating.objects.filter(rater_id=self.id).aggregate(Avg('score'))

    def get_total(self):
        return Rating.objects.filter(rater_id=self.id).aggregate(Count('score'))


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)

    def __str__(self):
        return ("{}: {} by {}".format(self.movie,
                                      self.score, self.rater))

    def get_movie_name(self):
        movie = Movie.objects.get(id=self.movie_id)
        return movie.title
