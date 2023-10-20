from django.contrib import admin
from app.movie.models import *


# Register your models here.
admin.site.register(Movie)
admin.site.register(Channel)
admin.site.register(Genre)