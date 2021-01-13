import logging
from pathlib import Path

from PIL import Image
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
import numpy as np

from classifier.classifier import ClassifierModel
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
    classifier = ClassifierModel(model_file_path=Path("classifier/final_EfficientNetB0.h5"))

    def perform_create(self, serializer):
        # Call classifier here
        image_field = serializer.validated_data['snake_image']
        image = Image.open(image_field.image.path)

        predictions = self.classifier.predict(image)
        logging.debug(f"predictions = {predictions}")

        top_1_class = np.argmax(predictions)
        top_1_species = (list(self.classifier.class_dictionary.keys())[
                  list(self.classifier.class_dictionary.values()).index(top_1_class)])
        logging.warning(f"Top 1 species = {top_1_species}")

        classification_id = 1

        snake_class = SnakeInfo.objects.filter(latin_name=top_1_species).first()
        if snake_class is not None:
            classification_id = snake_class.id
        print(snake_class)

        classification = SnakeInfo.objects.get(id=classification_id)
        serializer.save(classification=classification)
