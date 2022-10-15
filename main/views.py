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
    if request.user.is_authenticated:
        usuario = User.objects.get(pk=request.user.pk)
        return redirect('gb:confirmed', usuario.pk)
    return render(request, 'gb/index.html')

def loginPage(request):
    if(request.method == 'POST'):

        user = authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            usuario = User.objects.get(pk=request.user.pk)
            return redirect('gb:confirmed', usuario.pk)
        else:
            messages.info(request, "Usuário ou senha incorretos.")

    return render(request,'gb/login.html')

def logoutUser(request):
    logout(request)
    return redirect('gb:index')

def register(request):
    instance = User()
    if request.user.is_authenticated:
        instance = User.objects.get(pk = usuario.pk)

    form = CreateFormUser(request.POST, instance=instance)
    if request.method == 'POST':
        #if preencheu == False:
        
        #else:
            #form = CreateFormUser(request.POST, instance=User.objects.get(pk=usuario.pk))
        if form.is_valid():

            form.save()

            '''user = form.cleaned_data.get('username')
            messages.success(request, 'A conta foi criada para ' + user'''

            user = authenticate(username=form.cleaned_data['username'],
            password = form.cleaned_data['password1']
            ) 
            usuario = User.objects.get(pk=user.pk)
            
            login(request, user)
            return redirect('gb:caracteristicas', usuario.pk)
            #return redirect('gb:metas')
            
    context = {'form':form}
    return render(request, 'gb/register.html', context)

def define_caracteristicas(request,pk):
    instance = Caracteristicas()
    usuario = User.objects.get(pk=pk)
    form = CaracteristicasForm(request.POST or None, instance=instance)
    form_agua = IngestaoAguaForm()
    form_calorias = IngestaoCaloriasForm()
    if request.POST and form.is_valid():
        obj = form.save(commit=False) 
        obj.usuario = usuario
        obj.peso_inicial = obj.peso_atual
        obj.save()

        obj_agua = form_agua.save(commit=False)
        obj_agua.usuario = usuario
        obj_agua.agua = 0
        obj_agua.save()

        obj_calorias = form_calorias.save(commit=False)
        obj_calorias.usuario = usuario
        obj_calorias.calorias = 0
        obj_calorias.save()
        return redirect('gb:define_metas', usuario.pk)
    
    context = {'usuario':usuario, 'form': form}
    return render(request,'gb/caracteristicas.html', context)

def define_metas(request, pk):
    instance = Metas()
    usuario = User.objects.get(pk=pk)
    form = MetasForm(request.POST or None, instance=instance)
    
    if request.POST and form.is_valid():
        obj = form.save(commit=False)
        obj.usuario = usuario
        obj.save()

        return redirect('gb:confirmed', usuario.pk)
    
    context = {'usuario':usuario, 'form': form}
    return render(request,'gb/define_metas.html', context)

def metas(request, pk):
    usuario = User.objects.get(pk=pk)
    metas = Metas.objects.get(pk = usuario.pk)
    context = {'usuario': usuario, 'metas': metas} 
    return render(request, "gb/metas_info.html", context)

def edit_metas(request, pk):
    usuario = User.objects.get(pk=pk)
    instance = Metas.objects.get(pk = usuario.pk)
    
    form = MetasForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        obj = form.save(commit=False) 
        obj.usuario = usuario
        obj.save()

        return redirect('gb:metas_info', usuario.pk)
    
    context = {'usuario':usuario,  'form': form}
    return render(request,'gb/metas_edit.html', context)

def peso(request, pk):
    pessoa = User.objects.get(pk=pk)
    metas = Metas.objects.get(pk = pessoa.pk)
    caracteristicas = Caracteristicas.objects.get(pk = pessoa.pk)
    historico = PesoHistory.objects.filter(usuario_id=pessoa.pk)
    
    form_history = PesoHistoryForm(request.POST or None)
    form = PesoForm(request.POST or None, instance=caracteristicas)
    if request.POST and form.is_valid() and form_history.is_valid():
        obj = form.save(commit=False) 
        obj.usuario = pessoa
        obj.altura = caracteristicas.altura
        obj.idade = caracteristicas.idade

        obj_history = form_history.save(commit=False) 
        obj_history.usuario = pessoa
        obj_history.peso = form.cleaned_data['peso_atual']

        obj_history.save()
        obj.save()

        return redirect('gb:peso', pessoa.pk)

    context = {'pessoa':pessoa, 'metas': metas, 'caracteristicas': caracteristicas, 'historico': historico, 'form': form}    
    return render(request, "gb/peso.html", context)

def peso_entry(request, pk):
    usuario = User.objects.get(pk=pk)
    instance = Caracteristicas.objects.get(pk=pk)

    context = {'usuario':usuario}
    return render(request,'gb/peso_entry.html', context)

def water_count(request, pk):
    usuario = User.objects.get(pk=pk)
    form = IngestaoAguaForm()
    instance = IngestaoAgua.objects.get(pk=usuario.pk)
    instance_last_date = IngestaoAgua.objects.latest('created')
    metas = Metas.objects.get(pk=usuario.pk)
    bateu_meta = False
    if(instance_last_date.get_day > instance.get_day):
        consumo = 0
    else:
        keep = instance.agua
        consumo = keep

    dia = instance.get_day
    mes = instance.get_month
    
    um_dig = False

    if len(str(dia)) == 1:
        um_dig = True 

    falta = (metas.agua *1000) - consumo
    if falta<=0:
        bateu_meta=True
        falta = falta * (-1)
    if request.method == 'POST':
        form = IngestaoAguaForm(request.POST or None, instance=instance)
        if form.is_valid():
            consumo = form.cleaned_data['agua'] + keep
            falta = (metas.agua *1000) - consumo
            obj = form.save(commit=False)
            obj.agua = consumo
            obj.usuario = usuario
            obj.save()
            
        
        return redirect('gb:agua', usuario.pk)
    context = {'usuario':usuario, 'form':form, 'consumo':consumo, 'falta':falta, 'dia':dia, 'mes':mes, 'um_dig':um_dig, 'bateu_meta':bateu_meta}
    return render(request, 'gb/agua.html',context)

def calorie_count(request, pk):
    usuario = User.objects.get(pk=pk)
    form = IngestaoCaloriasForm()
    instance = IngestaoCalorias.objects.get(pk=usuario.pk)
    instance_last_date = IngestaoCalorias.objects.latest('created')
    metas = Metas.objects.get(pk=usuario.pk)
    bateu_meta = False
    if(instance_last_date.get_day > instance.get_day):
        consumo = 0
    else:
        keep = instance.calorias
        consumo = keep

    dia = instance.get_day
    mes = instance.get_month
    
    um_dig = False

    if len(str(dia)) == 1:
        um_dig = True 

    falta = metas.calorias - consumo
    if falta<=0:
        bateu_meta=True
        falta = falta * (-1)
    if request.method == 'POST':
        form = IngestaoCaloriasForm(request.POST or None, instance=instance)
        if form.is_valid():
            consumo = form.cleaned_data['calorias'] + keep
            falta = metas.calorias - consumo
            obj = form.save(commit=False)
            obj.calorias = consumo
            obj.usuario = usuario
            obj.save()
            
        
        return redirect('gb:calorias', usuario.pk)
    context = {'usuario':usuario, 'form':form, 'consumo':consumo, 'falta':falta, 'dia':dia, 'mes':mes, 'um_dig':um_dig, 'bateu_meta':bateu_meta}
    return render(request, 'gb/calorias.html',context)

# confirm test
def confirmed(request, pk=None):
    if pk:
        usuario = User.objects.get(pk=pk)
    else:
        usuario = User.objects.get(pk=request.user.pk)
    if not request.user.is_authenticated:
        return redirect('gb:register', usuario.pk)
    
    metas = Metas.objects.get(pk=usuario.pk)
    caracteristicas = Caracteristicas.objects.get(pk=usuario.pk)
    ingestao_agua = IngestaoAgua.objects.get(pk=usuario.pk)
    ingestao_calorias = IngestaoCalorias.objects.get(pk=usuario.pk)
    context = {'usuario':usuario, "metas": metas, "caracteristicas": caracteristicas, 'ingestao_agua':ingestao_agua, 'ingestao_calorias':ingestao_calorias}
    return render(request,'gb/confirmed.html', context)


def csrf_failure(request, reason=""):
    context = {'message': 'some custom messages'}
    return render('gb/errocsrf.html' , context)