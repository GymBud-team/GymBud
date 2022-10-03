#Imports
# Imports
import sqlite3
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from datetime import date, timedelta

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

def define_caracteristicas(request):
    instance = Caracteristicas()
    
    form = CaracteristicasForm(request.POST or None, instance=instance)
    form_agua = IngestaoForm()
    if request.POST and form.is_valid():
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.usuario = request.user # Add an author field which will contain current user's id
        obj.peso_inicial = obj.peso_atual
        obj.save()

        obj_agua = form_agua.save(commit=False)
        obj_agua.usuario = request.user
        obj_agua.agua = 0
        obj_agua.save()
        return redirect('gb:define_metas')
    
    context = {'form': form}
    return render(request,'gb/caracteristicas.html', context)

def define_metas(request):
    instance = Metas()
    
    form = MetasForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.usuario = request.user # Add an author field which will contain current user's id
        obj.save()

        return redirect('gb:confirmed')
    
    context = {'form': form}
    return render(request,'gb/define_metas.html', context)

def metas(request):
    
    metas = Metas.objects.get(id = request.user.id)
    context = {'metas': metas} 
    return render(request, "gb/metas_info.html", context)

def edit_metas(request):
    instance = Metas.objects.get(id = request.user.id)
    
    form = MetasForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.usuario = request.user # Add an author field which will contain current user's id
        obj.save()

        return redirect('gb:metas_info')
    
    context = {'form': form}
    return render(request,'gb/metas_edit.html', context)

def peso(request):
    metas = Metas.objects.get(id = request.user.id)
    caracteristicas = Caracteristicas.objects.get(id = request.user.id)
    historico = PesoHistory.objects.filter(usuario_id= request.user.id)
    
    form_history = PesoHistoryForm(request.POST or None)
    form = PesoForm(request.POST or None, instance=caracteristicas)
    if request.POST and form.is_valid() and form_history.is_valid():
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.usuario = request.user # Add an author field which will contain current user's id
        obj.altura = caracteristicas.altura
        obj.idade = caracteristicas.idade

        obj_history = form_history.save(commit=False) # Return an object without saving to the DB
        obj_history.usuario = request.user
        obj_history.peso = form.cleaned_data['peso_atual']

        obj_history.save()
        obj.save()

        return redirect('gb:peso')

    context = {"metas": metas, "caracteristicas": caracteristicas, 'historico': historico, 'form': form}    
    return render(request, "gb/peso.html", context)

def peso_entry(request):
    instance = Caracteristicas.objects.get(id = request.user.id)

    context = {}
    return render(request,'gb/peso_entry.html', context)

def water_count(request):
    form = IngestaoForm()
    instance = Ingestao.objects.get(id = request.user.id)
    instance_last_date = Ingestao.objects.latest('created')
    metas = Metas.objects.get(id = request.user.id)
    bateu_meta = False
    if(instance_last_date.get_day > instance.get_day):
        consumo = 0
    else:
        keep = instance.agua
        consumo = keep

    dia = instance.get_day
    mes = instance.get_month
    
    if len(str(dia)) == 1:
        um_dig = True 

    falta = (metas.agua *1000) - consumo
    if falta<=0:
        bateu_meta=True
        falta = falta * (-1)
    if request.method == 'POST':
        form = IngestaoForm(request.POST or None, instance=instance)
        if form.is_valid():
            consumo = form.cleaned_data['agua'] + keep
            falta = (metas.agua *1000) - consumo
            obj = form.save(commit=False)
            obj.agua = consumo
            obj.usuario = request.user
            obj.save()
            

        return redirect('gb:agua')
    context = {'form':form, 'consumo':consumo, 'falta':falta, 'dia':dia, 'mes':mes, 'um_dig':um_dig, 'bateu_meta':bateu_meta}
    return render(request, 'gb/agua.html',context)

# confirm test
def confirmed(request):
    metas = Metas.objects.get(id = request.user.id)
    caracteristicas = Caracteristicas.objects.get(id = request.user.id)
    ingestao = Ingestao.objects.get(id = request.user.id)

    context = {"metas": metas, "caracteristicas": caracteristicas, 'ingestao':ingestao}
    return render(request,'gb/confirmed.html', context)
