from rest_framework import serializers
from .models import *


# Create your models here.
class BaseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        Model = self.context.get('view').get_serializer_class().Meta.model
        user = self.context.get('request').user

        company_id = self.context['request'].auth['company']
        validated_data['created_by'] = user
        validated_data['updated_by'] = user

        if getattr(Model, 'company', None):
            validated_data['company_id'] = company_id

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
        exclude = ['created_by', 'updated_by']


class EconomicActivitySerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = EconomicActivity


class CompanyGroupSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = CompanyGroup


class CompanySerializer(BaseSerializer):
    economic_activity = EconomicActivitySerializer(read_only=True)
    economic_activity_id = serializers.IntegerField(write_only=True)

    group = CompanyGroupSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)


    class Meta(BaseSerializer.Meta):
        model = Company


class UserCompanySerializer(serializers.Serializer):
    id = serializers.CharField()
    unique_id = serializers.CharField()
    name = serializers.CharField()


class BranchAddresSerializer(BaseSerializer):
    branch = serializers.CharField(read_only=True)
    branch_id = serializers.CharField(write_only=True)

    class Meta(BaseSerializer.Meta):
        model = BranchAddress


class BranchSerializer(BaseSerializer):
    company = CompanySerializer(read_only=True)
    branchaddress = BranchAddresSerializer(read_only=True)
    branchaddress_id = serializers.CharField(write_only=True)

    class Meta(BaseSerializer.Meta):
        model = Branch


class MediaResourceSerializer(BaseSerializer):
    content = serializers.FileField()

    class Meta(BaseSerializer.Meta):
        model = MediaResource
