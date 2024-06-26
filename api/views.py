from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer, RatingSerializer
from .models import Movie, Rating


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
