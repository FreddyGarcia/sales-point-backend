from django.urls import path, include
from rest_framework import routers
from . import api
from . import viewsets

router = routers.DefaultRouter()

router.register('product-families', api.ProductFamilyViewSet)
router.register('product-lines', api.ProductLineViewSet)
router.register('product-measure-units', api.ProductMeasureUnitViewSet)
router.register('products', api.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]