from django.urls import path
from .views import listado_estudiantes, listado_cursos

urlpatterns = [
    path('estudiantes/', listado_estudiantes, name='listado_estudiantes'),
    path('cursos/', listado_cursos, name='listado_cursos'),
]