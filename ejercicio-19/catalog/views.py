from django.shortcuts import render
from .models import Genre, Director, Movie

# Create your views here.

def catalog(request):
    query_values = ('id', 'title', 'sypnosis', 'director__first_name', 'director__last_name', 'genre__name')
    all_movies = Movie.objects.all().values(*query_values)
    movies_dict = {}
    for m in all_movies:
        mid = str(m['id'])
        if not mid in movies_dict:
            movies_dict[mid] = {
                'title': m['title'],
                'sypnosis': m['sypnosis'],
                'director': f'{m["director__first_name"]} {m["director__last_name"]}',
                'genres': [m['genre__name']]
            }
        else:
            movies_dict[mid]['genres'].append(m['genre__name'])
            
    return render(request, 'catalog.html', {'movies': movies_dict})