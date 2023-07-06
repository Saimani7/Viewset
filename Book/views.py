from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentListViewsets(viewsets.ViewSet):
    def getlist(self,request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset,many = True)
        return Response(serializer.data)
    def createlist(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mgs':'completed data created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    def retrievelist(self,request,pk=None):
        id=pk
        if id is not None:
            queryset = Student.objects.get(id=id)
            serializer = StudentSerializer(queryset)
            return Response(serializer.data)
    def updatelist(self,request,pk):
        id=pk
        queryset = Student.objects.get(pk=id)
        serializer = StudentSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mgs':'completed data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroylist(self,request,pk):
        id=pk
        queryset = Student.objects.get(pk=id)
        queryset.delete()
        return Response({'mgz':'deleted'})



