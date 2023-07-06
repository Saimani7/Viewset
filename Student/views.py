from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Create your views here.
