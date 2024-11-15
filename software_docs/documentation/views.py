from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from django.views.generic import TemplateView, UpdateView, ListView
from .models import Artefacto, Especificacion
from .forms import ArtefactoForm, RegistroForm, EspecificacionForm
from django.urls import reverse_lazy


# Página de Inicio
class HomePageView(TemplateView):
    template_name = 'documentation/inicio.html'

# Crear artefacto - Vista basada en función
def CrearArtefactoView(request):
    if request.method == 'POST':
        form = ArtefactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_artefactos')
    else:
        form = ArtefactoForm()
    return render(request, 'documentation/crear_artefacto.html', {'form': form})

# Editar artefacto
class EditarArtefactoView(UpdateView):
    model = Artefacto
    form_class = ArtefactoForm
    template_name = 'documentation/editar_artefacto.html'
    success_url = reverse_lazy('lista_artefactos')

# Listar artefactos
class ListaArtefactosView(ListView):
    model = Artefacto
    template_name = 'documentation/lista_artefactos.html'
    context_object_name = 'artefactos'

def lista_artefactos(request):
    especificaciones = Especificacion.objects.all()
    return render(request, 'documentation/lista_artefactos.html', {'especificaciones': especificaciones})

# Vista de registro de usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Opcional: iniciar sesión después del registro
            messages.success(request, "Registro completado. ¡Bienvenido!")
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'documentation/registro.html', {'form': form})

# Vista para el dashboard
#def dashboard(request):
#    return render(request, 'documentation/dashboard.html')

# Vistas para cada tipo de artefacto
def requisitos(request):
    return render(request, 'documentation/requisitos.html')

def especificacion(request):
    if request.method == 'POST':
        form = EspecificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Especificación guardada con éxito.")
            return redirect('lista_artefactos')
    else:
        form = EspecificacionForm()
    return render(request, 'documentation/especificacion.html', {'form': form})

def diseno(request):
    return render(request, 'documentation/diseño.html')

def tecnica(request):
    return render(request, 'documentation/tecnica.html')

def pruebas(request):
    return render(request, 'documentation/pruebas.html')

def mantenimiento(request):
    return render(request, 'documentation/mantenimiento.html')

def usuarios_finales(request):
    return render(request, 'documentation/usuarios_finales.html')

def proceso(request):
    return render(request, 'documentation/proceso.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = "documentation/registration/password_reset_form.html"