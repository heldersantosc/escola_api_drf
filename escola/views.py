from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer


class AlunosViewSet(viewsets.ModelViewSet):

    # exibindo todos os alunos e alunos
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer