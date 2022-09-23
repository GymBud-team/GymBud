# Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateFormUser, MetasForm, CaracteristicasForm
from .models import Metas, Caracteristicas

# Landing Page
def index(request):
    return render(request, 'gb/index.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('gb:confirmed')
        
    else:
        if(request.method == 'POST'):

            user = authenticate(username=request.POST['username'], password = request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect('gb:confirmed')
            else:
                messages.info(request, "Usuário ou senha incorretos.")

    return render(request,'gb/login.html')

def logoutUser(request):
    logout(request)
    return redirect('gb:index')

def register(request):
    if request.user.is_authenticated:
        return redirect('gb:confirmed')

    else:
        form = CreateFormUser()
        if request.method == 'POST':
            form = CreateFormUser(request.POST)
            if form.is_valid():
                form.save()

                '''user = form.cleaned_data.get('username')
                messages.success(request, 'A conta foi criada para ' + user'''

                user = authenticate(username=form.cleaned_data['username'],
                password = form.cleaned_data['password1']
                ) 
        
                login(request, user)
                return redirect('gb:caracteristicas')
        #return redirect('gb:metas')
            
    context = {'form':form}
    return render(request, 'gb/register.html', context)

def caracteristicas(request):
    instance = Caracteristicas()
    
    form = CaracteristicasForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.usuario = request.user # Add an author field which will contain current user's id
        obj.save()

        return redirect('gb:metas')
    
    context = {'form': form}
    return render(request,'gb/metas.html', context)

def metas(request):
    instance = Metas()
    
    form = MetasForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.usuario = request.user # Add an author field which will contain current user's id
        obj.save()

        return redirect('gb:confirmed')
    
    context = {'form': form}
    return render(request,'gb/caracteristicas.html', context)


# confirm test
def confirmed(request):
    return render(request,'gb/confirmed.html')