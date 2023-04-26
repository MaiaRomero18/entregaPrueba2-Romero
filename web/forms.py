from django.forms import ModelForm
from .models import Alumnos, Profesor
     
class AlumnosForm(ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'nivel', 'mail', 'contrasena1', 'contrasena2']
        
class ProfesoresForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'mail', 'contrasena1', 'contrasena2']