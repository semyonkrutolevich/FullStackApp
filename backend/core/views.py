from django.http import JsonResponse
from core.models import Car

def all_cars(request):
    result = []
    cars = Car.objects.all()
    for car in cars:
        result.append({
            "vendor": car.vendor,
            "model": car.model,
            "year": car.year,
            "engine_volume": car.engine_volume,
        })

    return JsonResponse(result, safe=False)
