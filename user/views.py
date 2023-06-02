from django.shortcuts import render
from .serializers import Customer,CustomerSerializer
from rest_framework.viewsets import ModelViewSet

class CustomerViews(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
