from .models import employees
from rest_framework import serializers


class employeeSerialzers(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'

