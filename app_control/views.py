from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import pandas as pd
from .models import Certificaciones
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CertificacionesSerializer, Certificaciones
)
from rest_framework.response import Response
from datetime import datetime
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
    

class CertificationsCSVLoaderView(ModelViewSet):
    http_method_names = ('post',)
    queryset = certificacionView.queryset
    permission_classes = (IsAuthenticatedCustom,)
    serializer_class = CertificacionesSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.FILES['data']
        except Exception as e:
            raise Exception("You need to provide certifications CSV 'data'")

        certification_items = []

        try:
            csv_reader = csv.reader(codecs.iterdecode(data, 'utf-8'))
            for row in csv_reader:
                if not row[0]:
                    continue
                    
                # Check for empty values in other fields
                uid = row[0] or None
                org = row[1] or None
                work_location = row[2] or None
                certification = row[3] or None
                issue_date_str = row[4]  or None# Assuming the date is in string format

                # Convert the date format to YYYY-MM-DD
                if issue_date_str:
                    issue_date = datetime.strptime(issue_date_str, "%Y-%m-%d")
                else:
                    issue_date = None

                type = row[5] or None
                certification_items.append(
                    {
                        "uid": uid,
                        "org": org,
                        "work_location": work_location,
                        "certification": certification,
                        "issue_date": issue_date,
                        "type": type,
                    }
                )
        except csv.Error as e:
            raise Exception(e)

        if not certification_items:
            raise Exception("CSV file cannot be empty")

        data_validation = self.serializer_class(data=certification_items, many=True)
        data_validation.is_valid(raise_exception=True)
        data_validation.save()

        return Response({"success": "Certification items added successfully"})

