from django.urls import path
from . import views

app_name = 'gb'
urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name="logout"),
    path('agua/<str:pk>/',views.water_count, name="agua"),
        path('calorias/<str:pk>/',views.calorie_count, name="calorias"),
    path('caracteristicasform/<str:pk>/', views.define_caracteristicas, name='caracteristicas'),
    path('metasform/<str:pk>/', views.define_metas, name='define_metas'),
    path('metas/<str:pk>/', views.metas, name='metas_info'),
    path('metas/edit/<str:pk>/', views.edit_metas, name='metas_edit'),
    path('confirmed/<str:pk>/',views.confirmed, name='confirmed'),
    path('peso/<str:pk>/',views.peso, name='peso'),
    path('peso/entry/<str:pk>/',views.peso_entry, name='peso_entry'),
    path('createpost/<str:pk>/',views.create_post, name='create_post'),
    path('feed/',views.feed, name='feed')
]