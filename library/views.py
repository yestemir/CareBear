from typing import Tuple

from django.contrib.auth.models import User
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from library.models import HealthStatus, Checkbox, Checkboxes
from library.serializers import (
        UserSerializer, HealthCheckSerializer, CheckboxSerializer, CheckboxesSerializer
)


class HealthStatusViewSet(ModelViewSet):
    queryset: QuerySet = HealthStatus.objects.all()
    serializer_class = HealthCheckSerializer
    http_method_names = ('get', 'post')
    filter_backends: Tuple = (SearchFilter, DjangoFilterBackend)
    permission_classes = (IsAuthenticated,)
    # search_fields: Tuple = ('title', 'author')
    # filterset_fields: Tuple = ('genre_id',)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(
            user_id=request.user.pk
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CheckboxViewSet(ModelViewSet):
    queryset: QuerySet = Checkbox.objects.all()
    serializer_class = CheckboxSerializer
    http_method_names = ('get', 'post', 'patch')
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(
            user_id=request.user.pk
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CheckboxesViewSet(ModelViewSet):
    queryset: QuerySet = Checkboxes.objects.all()
    serializer_class = CheckboxesSerializer
    http_method_names = ('get', 'post')
    filter_backends: Tuple = (SearchFilter, DjangoFilterBackend)
    # search_fields: Tuple = ('text',)
    # filterset_fields: Tuple = ('book_id',)
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(
            user_id=request.user.pk
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# class SavedBookViewSet(ModelViewSet):
#     queryset: QuerySet = SavedBook.objects.all()
#     serializer_class = SavedBookSerializer
#     http_method_names = ('get', 'post', 'delete')
#     permission_classes = (IsAuthenticated,)
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset().filter(
#             user_id=request.user.pk
#         )
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class GenreViewSet(ModelViewSet):
#     queryset: QuerySet = Genre.objects.all()
#     serializer_class = GenreSerializer
#     http_method_names = ('get',)
#     filter_backends: Tuple = (SearchFilter,)
#     search_fields: Tuple = ('title',)


class UserViewSet(ModelViewSet):
    queryset: QuerySet = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post',)
    permission_classes = (AllowAny,)
