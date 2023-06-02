from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import Rezervation,RezervationSerializer,RezervationDetail,RezervationDetailSeralizer
from django.db.models import Max

last_id = Rezervation.objects.aggregate(max_id=Max('id'))['max_id']
mymodel = Rezervation.objects.only('visitor_number').get(pk=last_id)  # İlgili alanı yükle

deferred_attribute = mymodel.visitor_number  # DeferredAttribute özelliğine eriş

integer_value = int(deferred_attribute)  # Integera dönüştür
print(integer_value)

class RezervationViews(ModelViewSet):
    queryset=Rezervation.objects.all()
    serializer_class=RezervationSerializer

class ReservationDetailViews(ModelViewSet):
    queryset=RezervationDetail.objects.all()
    serializer_class=RezervationDetailSeralizer
    # def create(self, request):
    #     person_count = integer_value

    #     ages = []
    #     for i in range(person_count):
    #         age = int(request.data.get(f'person_age_{i+1}'))  # Her bir kişinin yaşını alın
    #         ages.append(age)

    #     return Response({'ages': ages})