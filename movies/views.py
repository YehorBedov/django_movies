from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie


class MoviesViews(ListView):
    '''Список фильмов'''
    movel = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'


class MovieDetailViews(DetailView):
    '''Побробное описание фильма'''
    # def get(self, request, pk):
    #     movie = Movie.objects.get(id=pk)
    #     return render(request, 'movie/movie_detail.html', {'movie':movie})
    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     return render(request, 'movies/movie_detail.html', {'movie':movie})
    model = Movie
    slug_field = 'url'



