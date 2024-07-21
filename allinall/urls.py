from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies import views

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    path('users/', include('users.urls')),
    path('movies/', include('movies.urls')),
    path('series/', include('series.urls')),
    path('', views.home, name = 'home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))