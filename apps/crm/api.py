from rest_framework import viewsets, permissions, filters
from .serializers import *
from .models import *
from apps.core.api import BaseViewSet

class CompanyGroupViewSet(BaseViewSet):
    queryset = CompanyGroup.active.all()
    serializer_class = CompanyGroupSerializer

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
