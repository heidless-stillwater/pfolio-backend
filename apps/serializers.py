from rest_framework import serializers
from .models import App, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class AppSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = App
        fields = ('name', 'description', 'link', 'image', 'tags')
