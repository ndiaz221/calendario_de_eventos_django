#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm  # Esto es lo correcto

#funcioon que nos mestra los eventos actuales
def get_events(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

#funcion que nos permite anadir eventos
def add_event(request):
    if request.method == 'POST':
        event = request.POST['event']
        category = request.POST['category']
        date = request.POST['date']
        Event.objects.create(event=event, category=category, date=date)
        return redirect('get_events')
    return render(request, 'add_event.html')

#funcion que nos permite acyualezar nuestros eventos
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)  # Vincula el formulario con la instancia del evento
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guarda el evento actualizado
            return redirect('get_events')  # Redirige a la lista de eventos (ajusta la URL si es necesario)
    else:
        form = EventForm(instance=event)  # Si es un GET, pasa la instancia al formulario para que se cargue con los datos actuales
    
    return render(request, 'update_event.html', {'form': form, 'event': event})



#funcion que nos permite eliminar los eventos


def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':  # Si es un POST, el evento se elimina
        event.delete()
        return redirect('get_events')  # Redirige de nuevo a la lista de eventos
    return render(request, 'delete_event.html', {'event': event})
