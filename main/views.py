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
    carac_last = Caracteristicas.objects.latest('usuario_id')
    metas_last = Metas.objects.latest('id')

    if request.user.is_authenticated and carac_last.usuario_id < request.user.id:
        return redirect('gb:caracteristicas')
    elif request.user.is_authenticated and metas_last.usuario_id < request.user.id:
        return redirect('gb:define_metas')
    elif request.user.is_authenticated:
        return redirect('gb:confirmed')

    return render(request, 'gb/index.html')

def loginPage(request):
    
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
    instance = User()
    if request.user.is_authenticated:
        instance = User.objects.get(id = request.user.id)
        return redirect('gb:caracteristicas')

    form = CreateFormUser(request.POST, instance=instance)
    if request.method == 'POST':
        #if preencheu == False:
        
        #else:
            #form = CreateFormUser(request.POST, instance=User.objects.get(pk=))
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
    carac_last = Caracteristicas.objects.latest('usuario_id')
    if request.user.is_authenticated and carac_last.usuario_id == request.user.id:
        return redirect('gb:define_metas')

    instance = Caracteristicas()
    
    
    form = CaracteristicasForm(request.POST or None, instance=instance)
    form_agua = IngestaoAguaForm()
    form_calorias = IngestaoCaloriasForm()
    if request.POST and form.is_valid():
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.usuario = request.user # Add an author field which will contain current user's id
        obj.peso_inicial = obj.peso_atual
        obj.save()

        obj_agua = form_agua.save(commit=False)
        obj_agua.usuario = request.user
        obj_agua.agua = 0
        obj_agua.save()

        obj_calorias = form_calorias.save(commit=False)
        obj_calorias.usuario = request.user
        obj_calorias.calorias = 0
        obj_calorias.save()
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
        obj = form.save(commit=False) 
        obj.usuario = request.user
        obj.save()

        return redirect('gb:metas_info')
    
    context = {'form': form}
    return render(request,'gb/metas_edit.html', context)

def peso(request, pk):
    metas = Metas.objects.get(id = request.user.id)
    caracteristicas = Caracteristicas.objects.get(id = request.user.id)
    historico = PesoHistory.objects.filter(usuario_id = request.user.id)
    
    form_history = PesoHistoryForm(request.POST or None)
    form = PesoForm(request.POST or None, instance=caracteristicas)
    if request.POST and form.is_valid() and form_history.is_valid():
        obj = form.save(commit=False) 
        obj.usuario = request.user
        obj.altura = caracteristicas.altura
        obj.idade = caracteristicas.idade

        obj_history = form_history.save(commit=False) 
        obj_history.usuario = request.user
        obj_history.peso = form.cleaned_data['peso_atual']

        obj_history.save()
        obj.save()

        return redirect('gb:peso')

    context = {'metas': metas, 'caracteristicas': caracteristicas, 'historico': historico, 'form': form}    
    return render(request, "gb/peso.html", context)

def peso_entry(request):
    instance = Caracteristicas.objects.get(id = request.user.id)

    context = {'usuario'}
    return render(request,'gb/peso_entry.html', context)

def water_count(request):
    form = IngestaoAguaForm()
    instance = IngestaoAgua.objects.get(id = request.user.id)
    instance_last_date = IngestaoAgua.objects.latest('created')
    metas = Metas.objects.get(id = request.user.id)
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
            obj.usuario = request.user
            obj.save()
            
        
        return redirect('gb:agua')
    context = {'form':form, 'consumo':consumo, 'falta':falta, 'dia':dia, 'mes':mes, 'um_dig':um_dig, 'bateu_meta':bateu_meta}
    return render(request, 'gb/agua.html',context)

def calorie_count(request):
    form = IngestaoCaloriasForm()
    instance = IngestaoCalorias.objects.get(id = request.user.id)
    instance_last_date = IngestaoCalorias.objects.latest('created')
    metas = Metas.objects.get(id = request.user.id)
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
            obj.usuario = request.user
            obj.save()
            
        
        return redirect('gb:calorias')
    context = {'form':form, 'consumo':consumo, 'falta':falta, 'dia':dia, 'mes':mes, 'um_dig':um_dig, 'bateu_meta':bateu_meta}
    return render(request, 'gb/calorias.html',context)

# confirm test
def confirmed(request):
    if not request.user.is_authenticated:
        return redirect('gb:register')
    
    metas = Metas.objects.get(id = request.user.id)
    caracteristicas = Caracteristicas.objects.get(id = request.user.id)
    ingestao_agua = IngestaoAgua.objects.get(id = request.user.id)
    ingestao_calorias = IngestaoCalorias.objects.get(id = request.user.id)
    context = {"metas": metas, "caracteristicas": caracteristicas, 'ingestao_agua':ingestao_agua, 'ingestao_calorias':ingestao_calorias}
    return render(request,'gb/confirmed.html', context)


def post(request, pk):
    post = Post.objects.get(id = pk)
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    new_comment = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.usuario = request.user
            obj.save()

    context = {'post': post, 'form':form, 'comments':comments}
    return render(request, 'gb/post.html', context)


def create_post(request):
    form = PostForm()
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.usuario = request.user
            obj.save()
        
            return redirect('gb:feed')
    context={'form':form}
    return render(request, 'gb/postForm.html', context)

def feed(request):
    posts = Post.objects.all()

    context={'posts':posts}
    return render(request, 'gb/feed.html', context)

def csrf_failure(request, reason=""):
    context = {'message': 'some custom messages'}
    return render('gb/errocsrf.html' , context)