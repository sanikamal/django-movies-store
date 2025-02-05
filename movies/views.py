from django.shortcuts import render
from .models import Movie

def index(request):
    search = request.GET.get('search')
    if search:
        movies = Movie.objects.filter(title__icontains=search)
    else:
        movies = Movie.objects.all()
    data = {}
    data['title'] = 'Movies'
    data['movies'] = movies

    return render(request, 'movies/index.html', {'data': data})

def show(request, id):
    data = {}
    movie = Movie.objects.get(id=id)
    data['title'] = movie.title
    data['movie'] = movie

    return render(request, 'movies/show.html', {'data': data})