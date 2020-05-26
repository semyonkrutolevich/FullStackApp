from django.urls import path

from core.views import CarViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cars', CarViewSet)

urlpatterns = router.urls