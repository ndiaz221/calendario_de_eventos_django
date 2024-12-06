#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm  # Esto es lo correcto


def get_events(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        event = request.POST['event']
        category = request.POST['category']
        date = request.POST['date']
        Event.objects.create(event=event, category=category, date=date)
        return redirect('get_events')
    return render(request, 'add_event.html')

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





''''def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.event = request.POST['event']
        event.category = request.POST['category']
        event.date = request.POST['date']
        event.save()
        return redirect('get_events')
    return render(request, 'update_event.html', {'event': event})'''


'''def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('get_events')'''

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':  # Si es un POST, el evento se elimina
        event.delete()
        return redirect('get_events')  # Redirige de nuevo a la lista de eventos
    return render(request, 'delete_event.html', {'event': event})