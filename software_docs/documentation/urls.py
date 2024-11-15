from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CustomPasswordResetView  # Importa la vista personalizada
from .views import HomePageView, EditarArtefactoView, ListaArtefactosView
from . import views

#Define las rutas para las vistas en la aplicación.
urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),  # Página de inicio
    path('registro/', views.registro, name='registro'), # registro usuarios
    path('login/', views.login, name='login'),  # Asegúrate de que también esté configurado el login
    path('artefactos/', ListaArtefactosView.as_view(), name='lista_artefactos'),
    path('crear/', views.CrearArtefactoView, name='crear_artefacto'),
    path('editar/<int:pk>/', EditarArtefactoView.as_view(), name='editar_artefacto'),
    # lista de artefactos para seleccionar 
    path('requisitos/', views.requisitos, name='requisitos'),
    path('especificacion/', views.especificacion, name='especificacion'),
    path('diseño/', views.diseno, name='diseño'),
    path('tecnica/', views.tecnica, name='tecnica'),
    path('pruebas/', views.pruebas, name='pruebas'),
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('usuarios-finales/', views.usuarios_finales, name='usuarios_finales'),
    path('proceso/', views.proceso, name='proceso'),
    path('crear_especificacion/', views.especificacion, name='crear_especificacion'),
    path('lista_artefactos/', views.lista_artefactos, name='lista_artefactos'),
# URLs para el restablecimiento de contraseña

    # Página de formulario de restablecimiento de contraseña
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='documentation/registration/password_reset_form.html'), 
         name='password_reset'),
    #path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # Página de confirmación de envío del correo
    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='documentation/registration/password_reset_done.html'), 
        name='password_reset_done'),
    
    # Página para confirmar la nueva contraseña
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='documentation/registration/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    
    # Página de finalización de restablecimiento
    path('reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='documentation/registration/password_reset_complete.html'), 
        name='password_reset_complete'),
    #path('editar-artefacto/<int:pk>/', EditarArtefactoView.as_view(), name='editar_artefacto'),
   

]
