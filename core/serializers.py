from rest_framework import serializers
from .models import *


# Create your models here.
class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_at', 'updated_at']


class CompanySerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Company


class BranchSerializer(BaseSerializer):
    company = CompanySerializer()

    class Meta(BaseSerializer.Meta):
        model = Branch


class company(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Company


class ProductLineSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = ProductLine


class ProductFamilySerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = ProductFamily


class ProductMeasureUnitSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = ProductMeasureUnit


class ProductSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Product
