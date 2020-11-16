from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from core.models import Company, MediaResource
from core.serializers import MediaResourceSerializer, UserCompanySerializer
from rest_framework import permissions


class MediaUploadViewSet(viewsets.ViewSet):

    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        queryset = MediaResource.api_objects.all()
        serializer = MediaResourceSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):

        file = request.FILES.get('file')

        if file:
            media = MediaResource()
            media.from_request(request)
            media.content = file
            media.save()
            serializer = MediaResourceSerializer(media)
            return Response(serializer.data)
        return Response('No file sent', status=500)


class UserCompanyViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk):
        queryset = Company.api_objects.filter(user__user__username=pk)
        serializer = UserCompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request):
        pass
