from django.shortcuts import render
from app1.models import Curso
from django.urls import path
from django.http import HttpResponse


def curso(self):
    curso = Curso(nombre="Python", curso=12943)
    curso.save()
    texto = f"----> Asignatura: {curso.nombre}, curso: {curso.curso}"
    return HttpResponse(texto)