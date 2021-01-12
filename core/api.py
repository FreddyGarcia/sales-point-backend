from rest_framework import viewsets, permissions, filters, pagination
from django.contrib.auth.models import Permission, Group
from rest_framework.decorators import action
from rest_framework.response import Response
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
    queryset = Company.api_objects.all()
    serializer_class = CompanySerializer


class BranchViewSet(BaseViewSet):
    queryset = Branch.api_objects.all()
    serializer_class = BranchSerializer


class BranchAddressViewSet(BaseViewSet):
    queryset = BranchAddress.api_objects.all()
    serializer_class = BranchAddresSerializer


class ProductFamilyViewSet(BaseViewSet):
    queryset = ProductFamily.api_objects.all()
    serializer_class = ProductFamilySerializer


class ProductLineViewSet(BaseViewSet):
    queryset = ProductLine.api_objects.all()
    serializer_class = ProductLineSerializer


class ProductMeasureUnitViewSet(BaseViewSet):
    queryset = ProductMeasureUnit.api_objects.all()
    serializer_class = ProductMeasureUnitSerializer


class ProductViewSet(BaseViewSet):
    queryset = Product.api_objects.all()
    serializer_class = ProductSerializer


class EconomicActivityViewSet(BaseViewSet):
    queryset = EconomicActivity.api_objects.all()
    serializer_class = EconomicActivitySerializer


class PermissionViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Permission.objects.all()
        serializer_class = queryset.values_list('name', flat=True)
        return Response(serializer_class) 

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter(username=pk).first()
        serializer_class = queryset.user_permissions.values_list('name', flat=True)
        return Response(serializer_class)  


class GroupViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Group.objects.all()
        serializer_class = queryset.values_list('name', flat=True)
        return Response(serializer_class) 

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter(username=pk).first()
        serializer_class = queryset.groups.values_list('name', flat=True)
        return Response(serializer_class)  
        