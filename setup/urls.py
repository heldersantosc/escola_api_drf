from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import (
    AlunosViewSet,
    CursosViewSet,
    MatriculaViewSet,
    ListaMatriculasAluno,
    ListaAlunosMatriculados,
)

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matriculas", MatriculaViewSet, basename="Matriculas")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("aluno/<int:pk>/matriculas/", ListaMatriculasAluno.as_view()),
    path("curso/<int:pk>/matriculas/", ListaAlunosMatriculados.as_view()),
]
