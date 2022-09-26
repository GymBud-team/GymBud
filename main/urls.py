from django.urls import path
from . import views

app_name = 'gb'
urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name="logout"),

    path('caracteristicasform/', views.define_caracteristicas, name='caracteristicas'),
    path('metasform/', views.define_metas, name='define_metas'),
    path('metas/', views.metas, name='metas_info'),
    path('metas/edit', views.edit_metas, name='metas_edit'),
    path('confirmed/',views.confirmed, name='confirmed'),
    path('peso/',views.peso, name='peso'),
    path('peso/entry',views.peso_entry, name='peso_entry'),
]