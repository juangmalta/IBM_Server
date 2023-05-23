from django.urls import path, include
from .views import certificacionView
from .views import CertificationsCSVLoaderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('certificaciones', certificacionView, 'certificaciones')

urlpatterns = [
    # Other URL patterns in your urls.py file
    path('certificaciones/upload/', CertificationsCSVLoaderView.as_view({'post': 'create'}), name='certificaciones-upload'),
]
