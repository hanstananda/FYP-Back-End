from rest_framework import serializers

from classifier.models import *


class SnakeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeImage
        fields = '__all__'


class SnakeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeInfo


class SnakeInfoReadSerializer(serializers.ModelSerializer):
    image = SnakeImageSerializer()

    class Meta:
        model = SnakeInfo
        fields = '__all__'


class ClassifySnakeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifySnakeRequest
        fields = '__all__'


class ExpertClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertClassification
        fields = '__all__'
