from django.contrib.auth.models import User
from django.forms import model_to_dict
from rest_framework import serializers
from django.db.models import Q
import datetime

from library.models import HealthStatus, Checkbox, Post, Comment


class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = ('id', 'name', 'title', 'done', 'everyday', 'type', 'health_status', 'user_id',)
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


def get_last_active_checkbox_data(user_id: int):
    health_status = HealthStatus.objects.filter(user_id=user_id).order_by('date').last()
    if health_status is None:
        return []
    checkbox_data = []
    for data in health_status.checkbox.all():
        if data.everyday is True:
            old_checkbox_data = model_to_dict(data)
            old_checkbox_data.pop('id')
            checkbox_data.append(old_checkbox_data)
    return checkbox_data


def update_all_active_checkbox_data(user_id: int, data, date):
    health_statuses = HealthStatus.objects.filter(user_id=user_id).filter(date__gte=date)
    print(health_statuses)
    for health_status in health_statuses:
        checkboxes = health_status.checkbox.all()
        checkbox = checkboxes.filter(name=data['name']).last()
        if checkbox is not None:
            checkbox.everyday = data['everyday']
            checkbox_data = model_to_dict(checkbox)
            Checkbox.objects.filter(pk=checkbox.id).update(**checkbox_data)
        else:
            if data['everyday']:
                new_data = data
                if data.get('id') is not None:
                    new_data.pop('id')
                new_data['health_status'] = health_status
                Checkbox.objects.create(**new_data)


class HealthCheckSerializer(serializers.ModelSerializer):
    checkbox = CheckboxSerializer(many=True)

    def create(self, validated_data):
        checkbox_data = validated_data.pop('checkbox')
        checkbox_data.extend(get_last_active_checkbox_data(validated_data.get('user')))
        health_status = HealthStatus.objects.create(**validated_data)
        health_status.save()
        for data in checkbox_data:
            data['health_status'] = health_status
            data['user_id'] = health_status.user
            Checkbox.objects.create(**data)
        return health_status

    def update(self, instance, validated_data):
        checkbox_data = validated_data.pop('checkbox')
        instance.mood_percentage = validated_data.get('mood_percentage', instance.mood_percentage)
        instance.mood = validated_data.get('mood', instance.mood)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        for data in checkbox_data:
            update_all_active_checkbox_data(validated_data.get('user'), data, validated_data.get('date', instance.date))
            data['health_status'] = instance
            data['user_id'] = instance.user
            if data.get('id') is not None:
                Checkbox.objects.filter(pk=data.pop('id')).update(**data)
            else:
                Checkbox.objects.create(**data)
        return instance

    class Meta:
        model = HealthStatus
        fields = (
            'id', 'date', 'mood_percentage', 'mood', 'comment', 'user', 'checkbox'
        )


class CommentSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    def get_username(self, obj):
        return obj.user.username

    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'created', 'user', 'username')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    def get_username(self, obj):
        return obj.user.username

    username = serializers.SerializerMethodField()

    def create(self, validated_data):
        comment_data = validated_data.pop('comment')
        post = Post.objects.create(**validated_data)
        post.save()
        for data in comment_data:
            data['post'] = post
            data['user'] = post.user
            # data['username'] = post.username
            Comment.objects.create(**data)
        return post

    def update(self, instance, validated_data):
        comment_data = validated_data.pop('comment')
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        for data in comment_data:
            data['post'] = instance
            data['user'] = instance.user
            if data.get('id') is not None:
                Comment.objects.filter(pk=data.pop('id')).update(**data)
            else:
                Comment.objects.create(**data)
        return instance

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'created', 'user', 'username', 'comment',
        )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = User(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # validated_data.pop('username')
        # validated_data.pop('email')
        instance = super().update(instance, validated_data)
        return instance
