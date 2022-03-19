from django.contrib.auth.models import User
from rest_framework import serializers

from library.models import HealthStatus, Checkbox, Checkboxes


class HealthCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthStatus
        fields = (
            'id', 'date', 'mood_percentage', 'mood', 'comment', 'nutrition', 'pills', 'todos', 'custom', 'user'
        )


class CheckboxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkboxes
        fields = ('id', 'title', 'checkboxes')


class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = ('id', 'task', 'done', 'everyday')


# class UserHealthStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserHealthStatus
#         fields = ('id', 'user', 'health_status')

# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ('id', 'title')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = User(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance
