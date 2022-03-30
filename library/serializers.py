from django.contrib.auth.models import User
from django.forms import model_to_dict
from rest_framework import serializers

from library.models import HealthStatus, Checkbox


class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = ('id', 'name', 'title', 'done', 'everyday', 'type', 'health_status', 'user_id',)
        # extra_kwargs = {
        #     "id": {
        #         "read_only": False,
        #         "required": False,
        #     },
        # }


class HealthCheckSerializer(serializers.ModelSerializer):
    checkbox = CheckboxSerializer(many=True)

    def create(self, validated_data):
        checkbox_data = validated_data.pop('checkbox')
        checkbox_data.extend(self.get_last_active_checkbox_data(validated_data.get('user')))
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
            # if data.get('id') is not None:
            #     Checkbox.objects.filter(pk=data.pop('id')).update(**data)
            # else:
            Checkbox.objects.create(**data)
        return instance

    def get_last_active_checkbox_data(self, user_id: int):
        health_status = HealthStatus.objects.filter(user_id=user_id).order_by('date').last()
        checkbox_data = []
        for data in health_status.checkbox.all():
            if data.everyday is True:
                old_checkbox_data = model_to_dict(data)
                old_checkbox_data.pop('id')
                checkbox_data.append(old_checkbox_data)
        return checkbox_data

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
