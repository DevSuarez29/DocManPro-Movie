from django.urls import path
from .views import *

urlpatterns = [
    path('MovieView/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('MovieView/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='movie-detail'),
    path('GenreView/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('GenreView/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='movie-detail'),
]
