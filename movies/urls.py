from django.urls import path
from movies import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('lists/', views.movie_list, name='movie_list'),
    path('details/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/add_review/', views.add_review, name='add_review'),
]
