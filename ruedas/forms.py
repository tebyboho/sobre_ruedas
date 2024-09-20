from django import forms
from .models import Unidad, Imagen

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['titulo', 'descripcion', 'marca', 'version', 'anio', 'kilometros','precio', 'vendido', 'visto']


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    


class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen']
        widgets = {
            'imagen' : MultipleFileInput()
        }
        '''widgets = {
            'imagen': forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
        }
        No se porque se esta forma no funciona, dejo la fuente: https://stackoverflow.com/questions/72591620/django-upload-multiple-images-per-post
        '''
