from django.shortcuts import render
from app.movie.models import Genre, Movie

def home(request):
    Logo = 'img/img/Logo.png'
    title = "DocManPro - Distribución Online de Cine, Musica, Artes y Noticias"
    genres = Genre.objects.all()[:5]

    return render(request, 'home.html', {
        'Logo': Logo,
        'title': title,
        'genres': genres
    })

def movie_detail(request, movie_id):
    Logo = 'img/img/Logo.png'
    title = "DocManPro - Distribución Online de Cine, Musica, Artes y Noticias"
    nombre = "Guest"
    movie = Movie.objects.get(id=movie_id)

    return render(request, 'page_movie.html', {
        'Logo': Logo,
        'title': title,
        'nombre': nombre, 
        'movie': movie
    })