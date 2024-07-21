from django.shortcuts import render, get_object_or_404, redirect
from series.models import Series, Review
from django.contrib.auth.decorators import login_required
from series.forms import SeriesReviewForm

def series_list(request):
    series = Series.objects.all()
    return render(request, 'series_list.html', {'series': series})

def series_detail(request, series_id):
    series = Series.objects.get(id=series_id)
    reviews = Review.objects.filter(series=series)

    if request.method == 'POST':
        form = SeriesReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.series = series
            review.save()
            return redirect('series:series_detail', series_id=series.id)
    else:
        form = SeriesReviewForm()

    return render(request, 'series_detail.html', {'series': series, 'reviews': reviews, 'form': form})



@login_required
def add_review(request, series_id):
    series = get_object_or_404(Series, id=series_id)

    if request.method == 'POST':
        form = SeriesReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.series = series
            review.save()
            return redirect('series:series_detail', series_id=series.id)
    else:
        form = SeriesReviewForm()

    return render(request, 'add_review.html', {'form': form, 'series': series})
