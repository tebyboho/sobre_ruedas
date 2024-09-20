from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image
import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator 
from .utils import get_current_year, get_years_tuple

class Unidad(models.Model):
    
    MARCAS_CHOICES = [
            ('Audi', 'Audi'),
            ('BMW', 'BMW'),
            ('Chery', 'Chery'),
            ('Chevrolet', 'Chevrolet'),
            ('Citroën', 'Citroën'),
            ('Dodge', 'Dodge'),
            ('Fiat', 'Fiat'),
            ('Ford', 'Ford'),
            ('Geely', 'Geely'),
            ('Great Wall', 'Great Wall'),
            ('Honda', 'Honda'),
            ('Hyundai', 'Hyundai'),
            ('JAC', 'JAC'),
            ('Jeep', 'Jeep'),
            ('Kia', 'Kia'),
            ('Land Rover', 'Land Rover'),
            ('Lifan', 'Lifan'),
            ('Mazda', 'Mazda'),
            ('Mercedes-Benz', 'Mercedes-Benz'),
            ('Mitsubishi', 'Mitsubishi'),
            ('Nissan', 'Nissan'),
            ('Peugeot', 'Peugeot'),
            ('Porsche', 'Porsche'),
            ('Ram', 'Ram'),
            ('Renault', 'Renault'),
            ('SsangYong', 'SsangYong'),
            ('Subaru', 'Subaru'),
            ('Suzuki', 'Suzuki'),
            ('Toyota', 'Toyota'),
            ('Volkswagen', 'Volkswagen')
    ]
    
    MOTOR_CHOICES = [
        
            (800, '0.8 L'),
            (1000, '1.0 L'),
            (1200, '1.2 L'),
            (1300, '1.3 L'),
            (1400, '1.4 L'),
            (1500, '1.5 L'),
            (1600, '1.6 L'),
            (1800, '1.8 L'),
            (2000, '2.0 L'),
            (2200, '2.2 L'),
            (2400, '2.4 L'),
            (2500, '2.5 L'),
            (2700, '2.7 L'),
            (3000, '3.0 L'),
            (3200, '3.2 L'),
            (3500, '3.5 L'),
            (3600, '3.6 L'),
            (4000, '4.0 L'),
            (4200, '4.2 L'),
            (4400, '4.4 L'),
            (4600, '4.6 L'),
            (5000, '5.0 L'),
            (5200, '5.2 L'),
            (5500, '5.5 L'),
            (6000, '6.0 L'),
            (6200, '6.2 L'),
            (6400, '6.4 L'),
            (7000, '7.0 L'),
            (7500, '7.5 L'),
            (8000, '8.0 L')
    ]

    MODELO_ANOS = get_years_tuple()

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, 
                                null = True,
                                blank = True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    marca = models.CharField(max_length=50, choices=MARCAS_CHOICES, default='Volkswagen')
    modelo = models.CharField(max_length=50, null=True, blank=True )
    version = models.CharField(max_length=70, null=True, blank=True)
    anio = models.IntegerField(choices=MODELO_ANOS, default=get_current_year(), verbose_name='año')
    kilometros = models.IntegerField(null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    vendido = models.BooleanField(default=False)
    visto = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    '''modelo (polo, virtus, etc) motor se reemplaza por version campo de texto'''
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['vendido']
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"


def validate_image(image):
    # Validar el tamaño máximo del archivo (por ejemplo, 2 MB)
    filesize = image.file.size
    max_size = 2 * 1024 * 1024  # 2 MB
    if filesize > max_size:
        raise ValidationError(f"El tamaño máximo permitido es de 2 MB. Su archivo tiene {filesize / (1024 * 1024):.2f} MB.")
    
    # Validar formatos permitidos (solo JPG y PNG)
    valid_extensions = ['jpg', 'jpeg', 'png']
    extension = image.name.split('.')[-1].lower()
    if extension not in valid_extensions:
        raise ValidationError("Solo se permiten archivos JPG y PNG.")


class Imagen(models.Model):
    unidad = models.ForeignKey(Unidad, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    descripcion = models.CharField(max_length=255, null=True, blank=True)
        
    def __str__(self):
        return f"Imagen de {self.unidad.titulo} - {self.unidad.usuario}"
    
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"