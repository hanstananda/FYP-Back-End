from rest_framework import serializers

from classifier.models import SnakeInfo, ClassifySnakeRequest, SnakeImage


class SnakeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeImage
        fields = '__all__'


class SnakeImageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeImage


class SnakeInfoSerializer(serializers.ModelSerializer):
    image = SnakeImageSerializer()

    class Meta:
        model = SnakeInfo
        fields = '__all__'


class ClassifySnakeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifySnakeRequest
        fields = '__all__'
