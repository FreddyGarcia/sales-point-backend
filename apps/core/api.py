from rest_framework.mixins import ListModelMixin
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters, pagination


class DefaultResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class BaseViewSet(viewsets.ModelViewSet, ListModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    pagination_class = DefaultResultsSetPagination

    def list(self, request):

        if request.auth is None:
            return Response(status=HTTP_401_UNAUTHORIZED)

        user_company_unique_id = request.auth['company']
        queryset = self.queryset.filter(company_id=user_company_unique_id)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
