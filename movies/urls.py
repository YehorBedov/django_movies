from django.urls import path
from . import views


urlpatterns = [
    path('', views.MoviesViews.as_view()),
    path('<slug:slug>/', views.MovieDetailViews.as_view(), name='movie_detail'),
]

