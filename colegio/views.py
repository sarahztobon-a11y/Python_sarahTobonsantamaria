from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Estudiante, Curso

@api_view(['GET'])
def listado_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    datos = [
        {
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
        }
        for estudiante in estudiantes
    ]
    return Response(datos)

@api_view(['GET'])
def listado_cursos(request):
    cursos = Curso.objects.all()
    datos = [
        {
            "id": curso.id,
            "nom_curso": curso.nom_curso,
        }
        for curso in cursos
    ]
    return Response(datos)