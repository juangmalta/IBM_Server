from django.db import models
from .models import Certificaciones
from user_control.serializers import CustomUserSerializer
from rest_framework import serializers


class CertificacionesSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    total_certifications = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certificaciones
        fields = '__all__'
