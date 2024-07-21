# users/urls.py
from django.urls import path
from users import views


app_name="users"

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
]
