from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data["username"],
            password=make_password(validated_data["password"]),
        )
        return user
