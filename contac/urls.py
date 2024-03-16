from django.urls import path
from . import views


urlpatterns = [
  path('',views.index, name="contac"),
  path('storage/<str:cargo>/<str:tareas>', views.storage, name="storage"),
  path('consultar/<int:id>', views.consultar, name="consultar"),
  path('actualizar/<str:nombre>/<int:id>/<str:mail>/<str:apellido>', views.actualizar, name="actualizar"),
  path('eliminar/<int:id>', views.eliminar, name="eliminar"),
  path('empleado/<int:id>/<str:name>/<str:mail>', views.empleado, name="empleado"),
  ]