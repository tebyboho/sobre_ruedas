from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Unidad, Imagen
from .forms import UnidadForm, ImagenForm

class Logueo(LoginView):
    template_name = 'ruedas/login.html'
    field = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('panel-admin')
    

class ListaUnidades(ListView):
    model = Unidad
    context_object_name = 'unidades'
    template_name = 'ruedas/lista_unidades.html'
    

class AdminPanel(LoginRequiredMixin, ListaUnidades):
    template_name = 'ruedas/admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidades'] = context['unidades'].filter(usuario=self.request.user)
        context['count'] = context['unidades'].filter(vendido=False).count()
        return context
        
        
class DetalleUnidad(DetailView):
    model = Unidad
    context_object_name = 'unidad'
    template_name = 'ruedas/unidad_detalle.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Obtengo imagenes asociadas a esta unidad
        context['imagenes'] = self.object.imagenes.all()
        return context
    
    def debug():
        print("Vengo de DetalleUnidad")
    
    

class CrearUnidad(LoginRequiredMixin, CreateView):
    model = Unidad
    fields = ['titulo', 'descripcion', 'marca', 'version', 'anio','kilometros','precio']
    success_url = reverse_lazy('panel-admin')
    template_name = 'ruedas/crear-unidad.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['imagenes_form'] = ImagenForm(self.request.POST, self.request.FILES)
        else:
            data['imagenes_form'] = ImagenForm()
        return data
       
    def form_valid(self, form):
        context = self.get_context_data()
        imagenes_form = context['imagenes_form']
        
        # Esteblezco el usuario para la unidad
        form.instance.usuario = self.request.user
        self.object = form.save() # Guardo la unidad 
        
        # Obtener las imágenes del formulario
        imagenes = self.request.FILES.getlist('imagen')
        
        if imagenes:
            for imagen in imagenes:
                # Crear una imagen para cada archivo cargado
                Imagen.objects.create(unidad=self.object, imagen=imagen)
                
        else:
            print(imagenes_form.errors)
        return super(CrearUnidad, self).form_valid(form)

class EditarUnidad(LoginRequiredMixin, UpdateView):
    model = Unidad
    fields = ['titulo', 'descripcion', 'marca', 'version', 'anio', 'precio', 'kilometros','vendido', 'visto']
    success_url = reverse_lazy('panel-admin')    
    template_name = 'ruedas/editar-unidad.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtenemos las imágenes asociadas a esta unidad
        context['imagenes'] = self.object.imagenes.all()  # La relación inversa que definiste
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super(EditarUnidad, self).form_valid(form)
        
        # Procesar nuevas imágenes
        nuevas_imagenes = self.request.FILES.getlist('imagenes')
        if nuevas_imagenes:
            for imagen in nuevas_imagenes:
                Imagen.objects.create(unidad=self.object, imagen=imagen)
            
        return response
    
class EliminarUnidad(LoginRequiredMixin, DeleteView):
    model = Unidad
    context_object_name = 'unidad'
    success_url = reverse_lazy('panel-admin') 


# Vista para eliminar imagen mientras se edita una unidad..
def eliminar_imagen(request, pk):
    
    imagen = get_object_or_404(Imagen, pk=pk)
    
    # Verificar si el usuario tiene permiso para eliminar la imagen
    if request.user == imagen.unidad.usuario:
        imagen.delete()
        return redirect('editar-unidad', pk=imagen.unidad.pk)
    else:
        return redirect('panel-admin')  # Redirigir si no tiene permiso
