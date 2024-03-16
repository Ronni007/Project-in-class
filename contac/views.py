from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from . models import contac
from . models import empleado


def empleado(response,name,apellido,mail,direccion,telefono,fecha):
  empleado = empleado (name=name,apellido=apellido,mail=mail,direccion=direccion,telefono=telefono,fecha=fecha)
  return HttpResponse("empleado registrado")


def index(response):
  contac = contac.objects.all ()
  for obj in contac:
   print( obj.asesor)
  return HttpResponse ('Lista de posts')


def storage(response, cargo, tarea ):
  contac = contac(cargo = cargo, tarea=tarea)
  contac.save()
  return HttpResponse("Guardamos los datos")
  
def consultar (request,id):
  empleado = empleado.objects.get(id=id)
  print(empleado)  
  return HttpResponse(f"empleado:{contac.name}, apellido:{contac.apellido}, Fecha:{contac.fecha}, Id:{contac.id}")

def actualizar(request,name,apellido,mail,telefono,direccion,fecha):
  contac = contac.objects.get(id=id)
  contac.name = name
  contac.save()
  return HttpResponse ("empleado actualizado")

def eliminar(request,id):
  contac = contac.objects.get(id=id)
  contac.delete()
  return HttpResponse("empleado eliminado")

def empleado(request,id,empleado):
  empleado = empleado.objects.get(id=id)
  empleado.objects.create
  