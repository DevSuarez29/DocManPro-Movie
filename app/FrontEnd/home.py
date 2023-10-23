from django.core.paginator import Paginator
from django.shortcuts import render
from app.movie.models import Genre, Movie

def home(request):
    Logo = 'img/img/Logo.png'
    title = "DocManPro - Distribución Online de Cine, Musica, Artes y Noticias"
    genres = Genre.objects.all()[:5]
    
    # Obtener todos los objetos Movie
    movies = Movie.objects.all()
    total_movies = movies.count()
    # Especifica la cantidad de elementos por página que deseas mostrar
    items_per_page = 18  # Puedes ajustar esto según tus necesidades
    
    # Inicializar el objeto Paginator
    paginator = Paginator(movies, items_per_page)
    
    # Obtener el número de página desde la solicitud GET (si está disponible)
    page_number = request.GET.get('page')
    
    # Obtener la página actual del paginador
    page = paginator.get_page(page_number)
    
    return render(request, 'home.html', {
        'Logo': Logo,
        'title': title,
        'genres': genres,
        'movies': page, 
        'total_movies':total_movies 
    })


def movie_detail(request, movie_id):
    Logo = 'img/img/Logo.png'
    title = "DocManPro - Distribución Online de Cine, Musica, Artes y Noticias"
    nombre = "Guest"
    movie = Movie.objects.get(id=movie_id)
    total_movies = Movie.objects.all().count()

    return render(request, 'page_movie.html', {
        'Logo': Logo,
        'title': title,
        'nombre': nombre, 
        'movie': movie,
        'total_movies':total_movies 
    })