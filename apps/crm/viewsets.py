from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from apps.crm.serializers import MediaResourceSerializer, UserCompanySerializer
from apps.crm.models import Company, MediaResource
from apps.core.api import BaseViewSet


class MediaUploadViewSet(BaseViewSet):

    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    queryset = MediaResource.active.all()
    serializer_class = MediaResourceSerializer

    def create(self, request):
        serializer = MediaResourceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('No file sent', status=status.HTTP_400_BAD_REQUEST)


class UserCompanyViewSet(viewsets.ViewSet):

    authentication_classes = []

    def retrieve(self, request, pk):

        user = User.objects.filter(username=pk).first()

        if user:
            companies = [ br.company for br in user.userprofile.branches.all()]
            serializer = UserCompanySerializer(companies, many=True)
            return Response(serializer.data)
        
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        return Response(status=status.HTTP_200_OK)
