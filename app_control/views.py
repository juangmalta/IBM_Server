from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import pandas as pd
from .models import Certificaciones
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CertificacionesSerializer, Certificaciones
)
from rest_framework.response import Response
from ibm_server.custom_methods import IsAuthenticatedCustom
from ibm_server.utils import CustomPagination, get_query
from django.db.models import Count, Sum, F
from django.db.models.functions import Coalesce, TruncMonth
from user_control.views import add_user_activity
from user_control.models import CustomUser
import csv
import codecs


class certificacionView(ModelViewSet):
    queryset = Certificaciones.objects.all()
    serializer_class = CertificacionesSerializer
    permission_classes = (IsAuthenticatedCustom,)
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset

        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)

        results = self.queryset.filter(**data)

        if keyword:
            search_fields = (
                "uid", "created_by__fullname", "created_by__email",
                "org", "certifications", "type", "work_location"
            )
            query = get_query(keyword, search_fields)
            return results.filter(query)

        return results

    def create(self, request, *args, **kwargs):
        
        return super().create(request, *args, **kwargs)
    
class excelImportView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']  # Nombre del campo en el formulario de la solicitud

        # Leer el archivo de Excel utilizando pandas
        df = pd.read_excel(file)

        # Realiza las operaciones necesarias con los datos del archivo
        for _, row in df.iterrows():
        # Create an instance of Certificaciones and populate it with data from the Excel row
            instance = Certificaciones(
                uid=row['uid'],
                org=row['org'],
                work_location=row['work_location'],
                certifications=row['certification'],
                issue_date=row['issue_date'],
                type=row['type'],
            )

        # Save the instance to the database
        instance.save()

        # Devuelve una respuesta apropiada
        return Response("Archivo de Excel importado correctamente.")
