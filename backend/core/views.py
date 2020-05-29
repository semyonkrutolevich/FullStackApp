from django.http import JsonResponse

from core.models import Car
from core.serializers import CarSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, CursorPagination


class CarsPagination(CursorPagination):
    page_size = 15
    ordering = 'id'

class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    pagination_class = CarsPagination

    def filter_queryset(self, queryset):
        for k,v in self.request.query_params.items():
            if k == "cursor":
                continue
            queryset = queryset.filter(**{k: v})
        return queryset