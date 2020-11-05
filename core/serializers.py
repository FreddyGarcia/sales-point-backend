from rest_framework import serializers
from .models import *


# Create your models here.
class BaseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        Model = self.context.get('view').get_serializer_class().Meta.model
        user = self.context.get('request').user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        obj = Model.objects.create(**validated_data)
        obj.save()
        return obj

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        instance.__dict__.update(validated_data)
        instance.updated_by = user
        instance.save()
        return instance

    class Meta:
        exclude = ['created_at', 'updated_at', 'is_enabled', 'created_by', 'updated_by']


class CompanySerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Company


class BranchAddresSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = BranchAddress


class BranchSerializer(BaseSerializer):
    company = CompanySerializer(read_only=True)
    branchaddress = BranchAddresSerializer()

    class Meta(BaseSerializer.Meta):
        model = Branch


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
