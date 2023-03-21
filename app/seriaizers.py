from .models import host
from rest_framework import serializers

class hostserializer(serializers.ModelSerializer):
    class Meta:
        model=host
        fields="__all__"