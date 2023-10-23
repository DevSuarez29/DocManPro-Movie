from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from app.movie.models import *
from .serializers import *

class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class GenreViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]

