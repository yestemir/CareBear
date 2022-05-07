from django.contrib.auth.models import User
from django.forms import model_to_dict
from rest_framework import serializers
from django.db.models import Q
import datetime

from library.models import HealthStatus, Checkbox, Post, Comment, UserBadge, \
    Test, TestAttempts, TestResults


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
    health_statuses = HealthStatus.objects.filter(user_id=user_id).filter(date__gt=date)
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
    comment = CommentSerializer(many=True, required=False)
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    def get_username(self, obj):
        return obj.user.username

    username = serializers.SerializerMethodField()

    def create(self, validated_data):
        comment_data = []
        if validated_data.get('comment') is not None:
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
        comment_data = []
        if validated_data.get('comment') is not None:
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


class UserBadgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBadge
        fields = ('id', 'badge', 'have_seen', 'current_days_steak', 'current_perfect_days_steak',
                  'current_good_days_steak', 'date', 'user',)
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class TestAttemptsSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = TestAttempts
        fields = ('id', 'user', 'result', 'date', 'test')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class TestResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        fields = ('id', 'user', 'min_result', 'max_result', 'title', 'test')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class TestSerializer(serializers.ModelSerializer):
    # test_attempts = TestAttemptsSerializer(many=True, required=False)
    # test_results = TestResultsSerializer(many=True, required=False)
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    # def create(self, validated_data):
    #     test_attempts_data = []
    #     test_results_data = []
    #     if validated_data.get('test_attempts') is not None:
    #         test_attempts_data = validated_data.pop('test_attempts')
    #
    #     if validated_data.get('test_results') is not None:
    #         test_results_data = validated_data.pop('test_results')
    #
    #     test = Test.objects.create(**validated_data)
    #     test.save()
    #
    #     for data in test_attempts_data:
    #         data['test'] = test
    #         data['user'] = test.user
    #         # data['username'] = post.username
    #         TestAttempts.objects.create(**data)
    #
    #     for data in test_results_data:
    #         data['test'] = test
    #         data['user'] = test.user
    #         # data['username'] = post.username
    #         TestResults.objects.create(**data)
    #
    #     return test
    #
    # def update(self, instance, validated_data):
    #     test_attempts_data = []
    #     test_results_data = []
    #     if validated_data.get('test_attempts') is not None:
    #         test_attempts_data = validated_data.pop('test_attempts')
    #
    #     if validated_data.get('test_results') is not None:
    #         test_results_data = validated_data.pop('test_results')
    #
    #     instance.questions = validated_data.get('questions', instance.text)
    #     instance.save()
    #     for data in test_attempts_data:
    #         data['post'] = instance
    #         data['user'] = instance.user
    #         if data.get('id') is not None:
    #             TestAttempts.objects.filter(pk=data.pop('id')).update(**data)
    #         else:
    #             TestAttempts.objects.create(**data)
    #
    #     for data in test_results_data:
    #         data['post'] = instance
    #         data['user'] = instance.user
    #         if data.get('id') is not None:
    #             TestResults.objects.filter(pk=data.pop('id')).update(**data)
    #         else:
    #             TestResults.objects.create(**data)
    #     return instance

    class Meta:
        model = Test
        fields = ('id', 'user', 'result', 'date')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


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
