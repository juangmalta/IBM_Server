from django.urls import path, include
from .views import certificacionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('certificaciones', certificacionView, 'certificaciones')
urlpatterns = [
    path('', include(router.urls)),
]
