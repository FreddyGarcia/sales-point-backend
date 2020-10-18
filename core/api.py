from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Company
    permission_classes = [permissions.IsAuthenticated]


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = Branch
    permission_classes = [permissions.IsAuthenticated]


class ProductFamilyViewSet(viewsets.ModelViewSet):
    queryset = ProductFamily.objects.all()
    serializer_class = ProductFamily
    permission_classes = [permissions.IsAuthenticated]


class ProductLineViewSet(viewsets.ModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLine
    permission_classes = [permissions.IsAuthenticated]


class ProductMeasureUnitViewSet(viewsets.ModelViewSet):
    queryset = ProductMeasureUnit.objects.all()
    serializer_class = ProductMeasureUnit
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product
    permission_classes = [permissions.IsAuthenticated]

