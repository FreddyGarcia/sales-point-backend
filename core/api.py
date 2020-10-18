from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(BaseViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class BranchViewSet(BaseViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class ProductFamilyViewSet(BaseViewSet):
    queryset = ProductFamily.objects.all()
    serializer_class = ProductFamilySerializer


class ProductLineViewSet(BaseViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer


class ProductMeasureUnitViewSet(BaseViewSet):
    queryset = ProductMeasureUnit.objects.all()
    serializer_class = ProductMeasureUnitSerializer


class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

