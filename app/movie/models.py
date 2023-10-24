import os
from django.db import models
from django.utils.text import slugify

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Género')
    description = models.TextField(verbose_name='Descripción del Género')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

class Channel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Canal')
    description = models.TextField(verbose_name='Descripción del Canal')
    url = models.URLField(max_length=200, verbose_name='URL del Canal')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Canales'

def upload_movie_poster(instance, filename):
    # Genera una ruta única para guardar cada archivo de póster
    ext = filename.split('.')[-1]
    filename = f'{instance.title}_{instance.id}.{ext}'
    return os.path.join('static/img/movie_posters/', filename)

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    release_date = models.DateField(verbose_name='Fecha de Lanzamiento')
    genre = models.ManyToManyField(Genre, verbose_name='Géneros')
    url_movie = models.URLField(max_length=200, verbose_name='URL de la película')
    description = models.TextField(verbose_name='Descripción')
    poster = models.CharField(max_length=200, verbose_name='Póster')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Canal Relacionado')
    slug = models.SlugField(unique=True, max_length=255, verbose_name='Slug', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Utiliza slugify para crear el slug
            original_slug = self.slug
            count = 1
            while Movie.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'