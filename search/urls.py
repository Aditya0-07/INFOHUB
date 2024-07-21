from django.urls import path
from search import views

app_name = "search"

urlpatterns = [
    path('', views.search, name='search'),
    path('search/', views.movie_search, name='movie_search'),
    path('suggest_movies/', views.suggest_movies, name='suggest_movies'),
]
