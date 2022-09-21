from django.urls import path
from . import views

app_name = 'gb'
urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('confirmed/',views.confirmed, name='confirmed'),
]