from __future__ import unicode_literals

from django.db import migrations
import csv
from datetime import date, datetime
from ratings.models import Movie, Rater


def import_movies(apps, schema_editor):
    with open('ratings/data/movies.csv', encoding='latin-1') as f:
        movies = csv.reader(f, delimiter="|")
        for row in movies:
            release = row[2]
            if release:
                release = datetime.strptime(release, "%d-%b-%Y").date()
            else:
                release = date(1200, 1, 1)

            movie = Movie(title=row[1],
                          release=release,
                          url=row[4])
            movie.save()


def import_raters(apps, schema_editor):
    with open('ratings/data/raters.csv', encoding='latin-1') as f:
        raters = csv.reader(f, delimiter="|")
        for row in raters:
            rater = Rater(age=row[1], sex=row[2], occupation=row[3])
            rater.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20160505_1958'),
    ]

    operations = [
        migrations.RunPython(import_movies),
        migrations.RunPython(import_raters),
    ]
