from django.urls import path, include
from .views import certificacionView
from .views import excelImportView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('certificaciones', certificacionView, 'certificaciones')
urlpatterns = [
    path('', include(router.urls)),
    path('import/', excelImportView.as_view(), name='excel-import'),
]
