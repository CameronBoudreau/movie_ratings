from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release = models.DateField()
    url = models.CharField(max_length=200, default="url")

    def __str__(self):
        return self.title


class Rater(models.Model):
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=200, default="sex")
    occupation = models.CharField(max_length=200, default="occupation")

    def __str__(self):
        print("{}: {} {} {}".format(self.id, self.age, self.sex,
                                    self.occupation))


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)

    def __str__(self):
        print("{}: {} by {}".format(self.movie_id, self.score, self.rater_id))
