import logging
from pathlib import Path
import random

from PIL import Image
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
import numpy as np

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from classifier.classifier import ClassifierModel
from classifier.serializers import *


class SnakeInfoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = SnakeInfo.objects.all()
    serializer_class = SnakeInfoReadSerializer


class SnakeInfoReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SnakeInfo.objects.all().exclude(name="Not Identified")
    serializer_class = SnakeInfoReadSerializer


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


class SnakeImageRandomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SnakeImage.objects.all()
    serializer_class = SnakeImageSerializer

    def list(self, request, *args, **kwargs):
        instance = random.choice(self.queryset)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ExpertClassificationViewSet(viewsets.ModelViewSet):
    queryset = ExpertClassification.objects.all()
    serializer_class = ExpertClassificationSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class SnakeReportViewSet(viewsets.ModelViewSet):
    queryset = SnakeReport.objects.all()
    serializer_class = SnakeReportSerializer
