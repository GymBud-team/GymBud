from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Vem com o gymbud")
