from django.contrib.auth.models import User
from rest_framework import serializers

from library.models import HealthStatus, Checkbox


class HealthCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthStatus
        fields = (
            'id', 'date', 'mood_percentage', 'mood', 'comment', 'checkboxes',
        )


# class CheckboxesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Checkboxes
#         fields = ('id', 'checkboxes')


class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = ('id', 'task', 'done', 'everyday')


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('id', 'book', 'user', 'created', 'text', 'rating')
#
#
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
