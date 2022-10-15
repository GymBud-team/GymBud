from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class CreateFormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MetasForm(ModelForm):
    class Meta:
        model = Metas
        fields = ['peso', 'calorias', 'agua']
        labels = {
            'agua': "Meta de ingestão diária de água:",
            'calorias':"Meta de consumo calórico diário:",
            'peso':"Meta de peso:"
        }
        

class CaracteristicasForm(ModelForm):
    class Meta:
        model = Caracteristicas
        fields = ['idade', 'peso_atual', 'altura']

        labels = {
            'peso_atual':"Peso atual:"
        }
    
class PesoForm(ModelForm):
    class Meta:
        model = Caracteristicas
        fields = ['peso_atual']

class PesoHistoryForm(ModelForm):
    class Meta:
        model = PesoHistory
        fields = []

class IngestaoAguaForm(ModelForm):
    class Meta:
        model = IngestaoAgua
        fields = ['agua']
    
class IngestaoCaloriasForm(ModelForm):
    class Meta:
        model = IngestaoCalorias
        fields = ['calorias']
