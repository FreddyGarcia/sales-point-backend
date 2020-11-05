from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register('branches', api.BranchViewSet)
router.register('branch-address', api.BranchAddressViewSet)
router.register('companies', api.CompanyViewSet)
router.register('product-families', api.ProductFamilyViewSet)
router.register('product-lines', api.ProductLineViewSet)
router.register('product-measure-units', api.ProductMeasureUnitViewSet)
router.register('products', api.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
