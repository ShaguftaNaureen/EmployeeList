from django.shortcuts import render, get_object_or_404
from .models import employees
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializers import employeeSerialzers


# Create your views here.
class employeeList(APIView):
    def get(self, response):
        model1 = employees.objects.all()
        serializer = employeeSerialzers()
        return Response(serializer.data)