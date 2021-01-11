from rest_framework import serializers
from .models import *
from apps.core.serializers import BaseSerializer


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

    class Meta(BaseSerializer.Meta):
        model = Branch


class MediaResourceSerializer(BaseSerializer):
    content = serializers.FileField()

    class Meta(BaseSerializer.Meta):
        model = MediaResource
