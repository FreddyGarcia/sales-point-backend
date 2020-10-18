from rest_framework import serializers
from django.db import models
from .models import *

# Create your models here.
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class ProductFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFamily
        fields = '__all__'


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = '__all__'


class ProductMeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMeasureUnit
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
