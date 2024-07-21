from django.urls import path
from series import views

app_name = 'series'

urlpatterns = [
    path('', views.series_list, name='series_list'),
    path('<int:series_id>/', views.series_detail, name='series_detail'),
    path('<int:movie_id>/add_review/', views.add_review, name='add_review'),
]

