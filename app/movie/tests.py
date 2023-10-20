from django.test import TestCase
from app.movie.models import *

query = Movie.objects.all()
print(query)

# Create your tests here.
