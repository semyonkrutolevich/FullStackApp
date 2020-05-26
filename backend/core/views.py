from django.http import JsonResponse

from core.models import Car
from core.serializers import CarSerializer

from rest_framework.viewsets import ModelViewSet


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
