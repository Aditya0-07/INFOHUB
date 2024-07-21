from django.shortcuts import render
from django.http import JsonResponse
from movies.models import Movie
from series.models import Series
from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
        series = Series.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.none()
        series = Series.objects.none()

    context = {
        'query': query,
        'movies': movies,
        'series': series,
    }
    return render(request, 'search_result.html', context)

def suggest_movies(request):
    query = request.GET.get('q', '')
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query))
        suggestions = [{'id': movie.id, 'title': movie.title} for movie in movies]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

def movie_search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        movies = Movie.objects.none()

    context = {
        'query': query,
        'movies': movies,
    }
    return render(request, 'movies/movie_search.html', context)
