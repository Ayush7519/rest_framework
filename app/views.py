from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import host
from .seriaizers import hostserializer
# Create your views here.

class hostcreateapiview(viewsets.ModelViewSet):
    queryset=host.objects.all()
    serializer_class=hostserializer
