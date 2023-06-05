from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterUserAPI.as_view()),
    path('login', views.LoginAPI.as_view()),
    path('logout', views.LogoutAPI.as_view()),
    path('logout-all', views.LogoutAllAPI.as_view()),
]