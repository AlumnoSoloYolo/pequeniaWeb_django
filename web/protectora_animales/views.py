from django.shortcuts import render
from .models import Colaborador, Animal, Protectora

# Create your views here.
def animal_list(request):
    animales = Animal.objects.all()
    return render(request, 'animales/animal_list.html', {'animal_mostrar': animales})

def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores/colaborador_list.html', {'colaborador_mostrar': colaboradores})

def protectora_list(request):
    protectoras = Protectora.objects.all()
    return render(request, 'protectoras/protectora_list.html', {'protectora_mostrar': protectoras})