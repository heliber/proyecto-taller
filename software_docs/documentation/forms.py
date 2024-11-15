from django import forms
#from .models import Proyecto
from ckeditor.widgets import CKEditorWidget
from .models import Artefacto
from .models import Especificacion # word
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

class ArtefactoForm(forms.ModelForm):
    class Meta:
        model = Artefacto
        fields = ['titulo', 'contenido', 'tipo_artefacto']

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# word
class EspecificacionForm(forms.ModelForm):
    class Meta:
        model = Especificacion
        fields = ['titulo', 'contenido']  # Aquí debes incluir los campos que quieres mostrar y el titulo

        widgets = {
            'contenido': forms.Textarea(attrs={'id': 'id_contenido'}),  # Asegúrate de que el ID coincide con el que usas en CKEditor
        }