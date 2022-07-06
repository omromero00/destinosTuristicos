from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    destino1 = Destination()
    destino1.name = 'Destino 1'
    destino1.price = 600
    destino1.desc = 'Sitio turisticos más sobresaliente'
    destino1.img = 'destination_1.jpg'
    destino1.offer = True

    destino2 = Destination()
    destino2.name = 'Destino 1'
    destino2.price = 600
    destino2.desc = 'Sitio turisticos más sobresaliente'
    destino2.img = 'destination_2.jpg'
    destino2.offer = False

    dests = [destino1, destino2]

    return render(request,'index.html',{
        'dests': dests,
    })