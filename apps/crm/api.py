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
    queryset = Company.active.all()
    serializer_class = CompanySerializer


class BranchViewSet(BaseViewSet):
    queryset = Branch.active.all()
    serializer_class = BranchSerializer


class BranchAddressViewSet(BaseViewSet):
    queryset = BranchAddress.active.all()
    serializer_class = BranchAddresSerializer


class EconomicActivityViewSet(BaseViewSet):
    queryset = EconomicActivity.active.all()
    serializer_class = EconomicActivitySerializer
