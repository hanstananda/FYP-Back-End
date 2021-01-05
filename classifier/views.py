from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view

from classifier.models import SnakeInfo, ClassifySnakeRequest, SnakeImage
from classifier.serializers import SnakeInfoSerializer, ClassifySnakeRequestSerializer, SnakeImageSerializer


class SnakeInfoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = SnakeInfo.objects.all()
    serializer_class = SnakeInfoSerializer


class SnakeImageViewSet(viewsets.ModelViewSet):
    queryset = SnakeImage.objects.all()
    serializer_class = SnakeImageSerializer


class ClassifySnakeRequestViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = ClassifySnakeRequest.objects.all()
    serializer_class = ClassifySnakeRequestSerializer

    def perform_create(self, serializer):
        # Call classifier here
        image = serializer.validated_data['snake_image']
        print(image)
        classification_id = 1
        classification = SnakeInfo.objects.get(id=classification_id)
        serializer.save(classification=classification)
