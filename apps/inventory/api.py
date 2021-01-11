from rest_framework import viewsets, permissions, filters
from rest_framework import pagination
from .serializers import *
from .models import *

from apps.core.api import BaseViewSet

class ProductFamilyViewSet(BaseViewSet):
    queryset = ProductFamily.active.all()
    serializer_class = ProductFamilySerializer


class ProductLineViewSet(BaseViewSet):
    queryset = ProductLine.active.all()
    serializer_class = ProductLineSerializer


class ProductMeasureUnitViewSet(BaseViewSet):
    queryset = ProductMeasureUnit.active.all()
    serializer_class = ProductMeasureUnitSerializer


class ProductViewSet(BaseViewSet):
    queryset = Product.active.all()
    serializer_class = ProductSerializer

