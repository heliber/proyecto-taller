from django.db import models
from ckeditor.fields import RichTextField # para editor word

class Artefacto(models.Model):
    TIPOS_ARTEFACTO = [
        ('requerimiento', 'Especificación de Requerimientos'),
        ('caso_uso', 'Diagramas de Casos de Uso'),
        ('prototipo', 'Prototipos'),
        ('plan_proyecto', 'Plan de Proyecto'),
        ('documentacion_tecnica', 'Documentación Técnica'),
        ('reporte', 'Reportes de Progreso'),
        ('manual_usuario', 'Manual de Usuario'),
        ('documentacion_mantenimiento', 'Documentación de Mantenimiento')
    ]

    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    tipo_artefacto = models.CharField(max_length=50, choices=TIPOS_ARTEFACTO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

#---------------------------------------------------------------------------#


# para el titulo
#class Especificacion(models.Model):
    #titulo = models.CharField(max_length=200)
    #contenido = models.TextField()

    #def __str__(self):
        #return self.titulo
#para el campo del area de texto para ingresar datos
class Especificacion(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = RichTextField()  # Campo de CKEditor para texto enriquecido