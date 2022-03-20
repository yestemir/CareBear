from django.contrib.auth.models import User
from rest_framework import serializers

from library.models import HealthStatus, Checkbox


# class CheckboxesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Checkboxes
#         fields = ('id', 'title', 'checkboxes')


class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = ('id', 'name', 'title', 'done', 'everyday', 'type', 'health_status', 'user_id')


class HealthCheckSerializer(serializers.ModelSerializer):
    checkbox = CheckboxSerializer(many=True)

    def create(self, validated_data):
        checkbox_data = validated_data.pop('checkbox')
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
            data['health_status'] = instance
            data['user_id'] = instance.user
            Checkbox.objects.create(**data)
        return instance

    class Meta:
        model = HealthStatus
        fields = (
            'id', 'date', 'mood_percentage', 'mood', 'comment', 'user', 'checkbox'
        )


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
