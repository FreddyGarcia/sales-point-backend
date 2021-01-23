from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from apps.crm.models import Company, MediaResource
from apps.crm.serializers import MediaResourceSerializer, UserCompanySerializer
from rest_framework import permissions
from rest_framework import status


class MediaUploadViewSet(viewsets.ViewSet):

    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        queryset = MediaResource.active.all()
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
