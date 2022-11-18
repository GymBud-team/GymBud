from django.urls import path
from . import views

app_name = 'gb'
urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name="logout"),
    path('agua/',views.water_count, name="agua"),
    path('calorias/',views.calorie_count, name="calorias"),
    path('caracteristicasform/', views.define_caracteristicas, name='caracteristicas'),
    path('metasform/', views.define_metas, name='define_metas'),
    path('metas/', views.metas, name='metas_info'),
    path('metas/edit/', views.edit_metas, name='metas_edit'),
    path('confirmed/',views.confirmed, name='confirmed'),
    path('peso/',views.peso, name='peso'),
    #path('peso/entry/',views.peso_entry, name='peso_entry'),
    path('createpost/',views.create_post, name='create_post'),
    path('feed/',views.feed, name='feed'),
    path('post/<int:pk>/', views.post, name="post"),
    path('like/<int:pk>', views.like_post, name="like_post"),
    path('requestworkout/', views.request_workout, name="requestWorkout")
]