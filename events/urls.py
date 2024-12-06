from django.contrib import admin
#from django.urls import path, include
#from . import views

#urlpatterns = [
#    path('admin/', admin.site.urls),
 #   path('', views.get_events, name='get_events'),
 #   path('add/', views.add_event, name='add_event'),
  #  path('delete/<int:id>/', views.delete_event, name='delete_event'),
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_events, name='get_events'),  # Página principal con todos los eventos
    path('add/', views.add_event, name='add_event'),  # Vista para agregar un evento
    path('update/<int:id>/', views.update_event, name='update_event'),  # Vista para actualizar un evento
    path('delete/<int:id>/', views.delete_event, name='delete_event'),  # Vista para eliminar un evento
    ]