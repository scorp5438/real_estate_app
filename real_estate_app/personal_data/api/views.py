from rest_framework import viewsets

from .serializers import PersonalDataSerializer, PersonalFullDataCreateXerializer, PersonalShortDataCreateXerializer
from ..models import PersonalData


class DataApiView(viewsets.ModelViewSet):
    serializer_class = PersonalDataSerializer
    queryset = PersonalData.objects.all()
    http_method_names = ['get']


class PersonalDataCreateApiView(viewsets.ModelViewSet):
    serializer_class = PersonalFullDataCreateXerializer
    queryset = PersonalData.objects.all()
    http_method_names = ['get', 'post']


class PersonalDataShortCreateApiView(viewsets.ModelViewSet):
    serializer_class = PersonalShortDataCreateXerializer
    queryset = PersonalData.objects.all()
    http_method_names = ['get', 'post']
