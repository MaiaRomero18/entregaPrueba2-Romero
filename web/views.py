from django.shortcuts import render
from .forms import AlumnosForm, ProfesoresForm
from .models import Alumnos, Profesor

def home(request):
    return render(request, 'home.html')

def cuenta(request):
    return render(request, 'cuenta.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': AlumnosForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cuenta')
            except IntegrityError:
                return render(request, 'signup.html', {'form': AlumnosForm, 'error': "Este usuario ya existe"})
        return render(request, 'signup.html', {'form': AlumnosForm, 'error': "Las contraseñas no coinciden"})









