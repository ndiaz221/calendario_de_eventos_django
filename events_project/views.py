from django.shortcuts import render

def index(request):
    events = []  # Aquí deberías obtener los eventos desde tu base de datos
    return render(request, 'index.html', {'events': events})
