from django.db import models

class Curso(models.Model):
    nom_curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_curso

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"