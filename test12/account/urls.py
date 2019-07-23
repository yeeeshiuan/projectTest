from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
