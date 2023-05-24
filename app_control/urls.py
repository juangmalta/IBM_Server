from django.urls import path, include
from .views import certificacionView
from .views import CertificationsCSVLoaderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('certificaciones', certificacionView, 'certificaciones'),
router.register('upload', CertificationsCSVLoaderView, 'upload')

urlpatterns = [
    # Other URL patterns in your urls.py file
    path('', include(router.urls)),
]
