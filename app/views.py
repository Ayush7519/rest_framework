from django.shortcuts import render
from rest_framework import generics
from .models import host
from .seriaizers import hostserializer
# Create your views here.

class hostcreateapiview(generics.CreateAPIView):
    queryset=host.objects.all()
    serializer_class=hostserializer
