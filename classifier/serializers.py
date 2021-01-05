from rest_framework import serializers

from classifier.models import SnakeInfo, ClassifySnakeRequest, SnakeImage


class SnakeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeInfo
        fields = '__all__'


class SnakeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeImage
        fields = '__all__'


class ClassifySnakeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifySnakeRequest
        fields = '__all__'
