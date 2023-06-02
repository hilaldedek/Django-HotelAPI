from rest_framework import serializers
from .models import Rezervation,RezervationDetail

class RezervationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rezervation
        fields='__all__'


class RezervationDetailSeralizer(serializers.ModelSerializer):
    class Meta:
        model=RezervationDetail
        fields='__all__'
