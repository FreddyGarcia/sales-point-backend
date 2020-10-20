from rest_framework import viewsets, permissions, filters
from rest_framework import pagination
from .serializers import *
from .models import *


class DefaultResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    pagination_class = DefaultResultsSetPagination


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

