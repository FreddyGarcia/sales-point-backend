from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register('branch', api.BranchViewSet)
router.register('company', api.CompanyViewSet)
router.register('branch', api.BranchViewSet)
router.register('product-family', api.ProductFamilyViewSet)
router.register('product-line', api.ProductLineViewSet)
router.register('product-measure-unit', api.ProductMeasureUnitViewSet)
router.register('product', api.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
