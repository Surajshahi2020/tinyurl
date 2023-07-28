from django.urls import path, include

from rest_framework.routers import DefaultRouter
from tinyapp.views import TinyViewSet


router = DefaultRouter()
router.register("Tinyurl", TinyViewSet, basename="demand")


urlpatterns = [
    path("", include(router.urls)),
]
