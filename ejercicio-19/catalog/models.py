from django.db import models
import uuid

# Create your models here.

class Genre(models.Model):
    GENRE_TYPES = (
        ('AC', 'Action'), ('AD', 'Adventure'), ('AN', 'Animation'), ('BI', 'Biography'),
        ('CO', 'Comedy'), ('CR', 'Crime'), ('DO', 'Documentary'), ('DR', 'Drama'),
        ('FA', 'Family'), ('FA', 'Fantasy'), ('FI', 'Film-Noir'), ('HI', 'History'),
        ('HO', 'Horror'), ('MU', 'Musical'), ('MY', 'Mystery'),
        ('RO', 'Romance'), ('SC', 'Sci-Fi'), ('SH', 'Short'), ('SP', 'Sport'),
        ('TH', 'Thriller'), ('WA', 'War'), ('WE', 'Western')
        )

    name = models.CharField(max_length=2, choices=GENRE_TYPES, blank=True, default=0)

    def __str__(self):
        for genre in self.GENRE_TYPES:
            if (self.name == genre[0]): return genre[1]
        return 'None'


class Director(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this movie')
    title = models.CharField(max_length=64)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    sypnosis = models.TextField(max_length=128, help_text='Brief summary of the movie')
    genre = models.ManyToManyField(Genre)
