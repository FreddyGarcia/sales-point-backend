from django.urls import path, include
from rest_framework import routers
from . import api
from . import viewsets

router = routers.DefaultRouter()
router.register('branch', api.BranchViewSet)
router.register('branch-address', api.BranchAddressViewSet)
router.register('company', api.CompanyViewSet)
router.register('product-family', api.ProductFamilyViewSet)
router.register('product-line', api.ProductLineViewSet)
router.register('product-measure-unit', api.ProductMeasureUnitViewSet)
router.register('product', api.ProductViewSet)
router.register('ecomic-activity', api.EconomicActivityViewSet)
router.register('media-upload', viewsets.MediaUploadViewSet, basename='media_upload')
router.register('user-company', viewsets.UserCompanyViewSet, basename='user_company')

urlpatterns = [
    path('', include(router.urls)),
]
