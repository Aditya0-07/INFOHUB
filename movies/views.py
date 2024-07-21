from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from movies.models import Movie, Review
from movies.forms import ReviewForm
from django.db.models import Q
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movies:movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()

    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form})

@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movies:movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'movie': movie})

