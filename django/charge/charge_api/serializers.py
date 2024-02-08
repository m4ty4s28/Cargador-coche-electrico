from rest_framework import serializers
from .models import ChargePoint

class ChargePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargePoint
        fields = ["id", "name", "status", "created_at", "deleted_at"]