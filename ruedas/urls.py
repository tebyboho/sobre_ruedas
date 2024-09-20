from django.urls import path
from .views import ListaUnidades, DetalleUnidad, CrearUnidad, EditarUnidad, EliminarUnidad, Logueo, AdminPanel, eliminar_imagen
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ListaUnidades.as_view(), name='unidades'),
    path('login/', Logueo.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), #next_page debe ser lista unidades?
    path('panel-admin/', AdminPanel.as_view(), name='panel-admin'),
    path('unidad/<int:pk>', DetalleUnidad.as_view(), name='unidad-detalle'),
    path('crear-unidad/', CrearUnidad.as_view(), name='crear-unidad' ),
    path('editar-unidad/<int:pk>', EditarUnidad.as_view(), name='editar-unidad'),
    path('eliminar-unidad/<int:pk>', EliminarUnidad.as_view(), name='eliminar-unidad'),
    path('eliminar-imagen/<int:pk>', eliminar_imagen, name='eliminar-imagen'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)