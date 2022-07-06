from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    destino1 = Destination()
    destino1.name = 'Destino 1'
    destino1.price = 600

    return render(request,'index.html',{
        'dest1': destino1,
    })
