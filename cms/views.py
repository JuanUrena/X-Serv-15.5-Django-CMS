from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Pages

# Create your views here.

def menu(request):
    return HttpResponse("Bienvenido al menu")
    
def page(request, name):
    try:
        data = Pages.objects.get(name=name)
        return HttpResponse(data.page)
    except Pages.DoesNotExist:
        return HttpResponse("Bienvenido a "+ name +" la pagina no existe")

