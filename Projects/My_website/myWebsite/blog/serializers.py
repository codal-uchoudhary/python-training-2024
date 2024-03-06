from rest_framework import serializers
from .models import Post, Tag, User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "caption"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class blogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = AuthorSerializer(required=False)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "excerpt",
            "image_name",
            "date",
            "slug",
            "content",
            "author",
            "tags",
        ]

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.author = self.context.get("request").user
        instance.tags.set(self.context.get("request").data["tags"])
        instance.save()
        return instance
