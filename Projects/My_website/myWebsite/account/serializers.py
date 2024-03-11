from rest_framework import serializers
from django.contrib.auth.models import User
from blog.serializers import blogSerializer
from .models import UserContent
from .utils import StrongPasswordValidator


class RegisterSerializers(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["username"]:
            if User.objects.filter(username=data["username"]).exists():
                raise serializers.ValidationError("username is exist")

        if data["email"]:
            if User.objects.filter(email=data["email"]).exists():
                raise serializers.ValidationError("email is exist")

        if data["password"]:
            status, message = StrongPasswordValidator(data["password"])
            if not status:
                raise serializers.ValidationError(message)

        return data

    def create(self, validate_data):
        user = User.objects.create_user(
            username=validate_data["username"],
            password=validate_data["password"],
            first_name=validate_data["first_name"],
            last_name=validate_data["last_name"],
            email=validate_data["email"],
        )
        user.set_password(validate_data["password"])
        user.save()
        return validate_data


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        if data["old_password"] == data["new_password"]:
            raise serializers.ValidationError(
                "new password is same as old password! choose diffeent password"
            )

        if data["new_password"]:
            status, message = StrongPasswordValidator(data["new_password"])
            if not status:
                raise serializers.ValidationError(message)

        return data


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if not data["password"] == data["password_confirm"]:
            return serializers.ValidationError("password is not matching")

        if data["password"]:
            status, message = StrongPasswordValidator(data["password"])
            if not status:
                raise serializers.ValidationError(message)

        return data


class GetBookmarkListSerializer(serializers.ModelSerializer):
    bookmarks = blogSerializer(many=True, read_only=True)

    class Meta:
        model = UserContent
        fields = ["bookmarks"]


class AddBookmarkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContent
        fields = []
