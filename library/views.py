from typing import Tuple

from django.contrib.auth.models import User
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .paginations import CustomPagination
from library.models import HealthStatus, Checkbox, Comment, Post
from library.serializers import (
        UserSerializer, HealthCheckSerializer, CheckboxSerializer, CommentSerializer, PostSerializer
)


class HealthStatusViewSet(ModelViewSet):
    pagination_class = CustomPagination
    queryset: QuerySet = HealthStatus.objects.all()
    serializer_class = HealthCheckSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    filter_backends: Tuple = (DjangoFilterBackend, )
    permission_classes = (IsAuthenticated,)
    search_fields: Tuple = ('date',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def filter_by_date_range(self, dates: dict, queryset):
        query_set = queryset
        if dates is None:
            return queryset
        if dates.get('start_date') is not None:
            query_set = query_set.filter(date__gte=dates.get('start_date'))
        if dates.get('end_date') is not None:
            query_set = query_set.filter(date__lte=dates.get('end_date'))
        return query_set

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(
            user=request.user.pk
        )
        print(request.query_params)
        queryset = self.filter_by_date_range(request.query_params, queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CheckboxViewSet(ModelViewSet):
    pagination_class = CustomPagination
    queryset: QuerySet = Checkbox.objects.all()
    serializer_class = CheckboxSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

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


class CommentViewSet(ModelViewSet):
    pagination_class = CustomPagination
    queryset: QuerySet = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def filter_post_id(self, post_id: dict, queryset):
        print(post_id, "aaaa")
        query_set = queryset
        if post_id is None:
            return queryset
        if post_id.get('post_id') is not None:
            query_set = Comment.objects.filter(post=post_id.get('post_id'))
        return query_set

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-created')
        queryset = self.filter_post_id(request.query_params, queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(ModelViewSet):
    pagination_class = CustomPagination
    queryset: QuerySet = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    filter_backends: Tuple = (DjangoFilterBackend, )
    permission_classes = (IsAuthenticated,)
    search_fields: Tuple = ('date',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-created')
        # print(request.query_params)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    pagination_class = CustomPagination
    queryset: QuerySet = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    permission_classes = (AllowAny,)

    @action(detail=False, methods=('patch', 'get'))
    def profile(self, request, pk=None):
        instance = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

