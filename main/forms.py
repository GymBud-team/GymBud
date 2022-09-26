from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Metas, Caracteristicas, PesoHistory

class CreateFormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MetasForm(ModelForm):
    class Meta:
        model = Metas
        fields = ['peso', 'calorias', 'agua']

class CaracteristicasForm(ModelForm):
    class Meta:
        model = Caracteristicas
        fields = ['idade', 'peso_atual', 'altura']
    
class PesoForm(ModelForm):
    class Meta:
        model = Caracteristicas
        fields = ['peso_atual']

class PesoHistoryForm(ModelForm):
    class Meta:
        model = PesoHistory
        fields = []