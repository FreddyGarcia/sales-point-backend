from django.urls import path, include
from rest_framework import routers
from . import api
from . import viewsets

router = routers.DefaultRouter()

router.register('branches', api.BranchViewSet)
router.register('branch-addresses', api.BranchAddressViewSet)
router.register('companies', api.CompanyViewSet)
router.register('ecomic-activities', api.EconomicActivityViewSet)
router.register('media-uploads', viewsets.MediaUploadViewSet, basename='media_upload')
router.register('user-companies', viewsets.UserCompanyViewSet, basename='user_company')

urlpatterns = [
    path('', include(router.urls)),
]
