from rest_framework import serializers
from .models import Example, ExampleTag


class ExampleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleTag
        fields = ('name',)


class ExampleSerializer(serializers.ModelSerializer):
    tags = ExampleTagSerializer(many=True)

    class Meta:
        model = Example
        fields = ('name', 'description', 'link', 'image', 'exampletags')
