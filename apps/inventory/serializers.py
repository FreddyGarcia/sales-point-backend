from rest_framework import serializers
from .models import *
from apps.core.serializers import BaseSerializer
from apps.crm.serializers import CompanySerializer


class ProductLineSerializer(BaseSerializer):
    company = CompanySerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = ProductLine


class ProductFamilySerializer(BaseSerializer):
    company = CompanySerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = ProductFamily


class ProductMeasureUnitSerializer(BaseSerializer):
    company = CompanySerializer(read_only=True)

    class Meta(BaseSerializer.Meta):
        model = ProductMeasureUnit


class ProductSerializer(BaseSerializer):
    unit = ProductMeasureUnitSerializer(read_only=True)
    family = ProductFamilySerializer(read_only=True)
    line = ProductLineSerializer(read_only=True)
    image = serializers.URLField(source='image.content', read_only=True)

    unit_id = serializers.IntegerField(write_only=True)
    image_id = serializers.IntegerField(write_only=True)
    family_id = serializers.IntegerField(write_only=True)
    line_id = serializers.IntegerField(write_only=True)

    class Meta(BaseSerializer.Meta):
        model = Product
        exclude = BaseSerializer.Meta.exclude
