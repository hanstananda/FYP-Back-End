import logging
from pathlib import Path

from tensorflow.python.keras.applications.efficientnet import EfficientNetB0
from tensorflow.python.keras.models import load_model
from tensorflow.keras import layers

import numpy as np

from PIL import Image


class ClassifierModel:
    _IMAGE_HEIGHT: int = 224
    _IMAGE_WIDTH: int = 224
    # Must change the following if classes changes!
    class_dictionary = {'Ahaetulla prasine': 0, 'Bungarus multicinctus': 1, 'Chrysopelea ornate': 2,
                        'Dendrelaphis pictus': 3, 'Psammodynastes pulverulentus': 5, 'Ptyas mucosa': 6,
                        'Rhabdophis subminiatus': 7, 'Trimeresurus albolabris': 8, 'Malayopython reticulatus': 4}

    def __init__(self,
                 logger_name: str = 'ML',
                 target_image_height: int = None,
                 target_image_width: int = None,
                 model_file_path: Path = None,
                 ):
        self.model = None
        self._logger = logging.getLogger(logger_name)

        if target_image_height is not None:
            self._IMAGE_HEIGHT = target_image_height
        if target_image_width is not None:
            self._IMAGE_WIDTH = target_image_width
        if model_file_path is not None:
            self.load_model(model_file_path)

        inputs = layers.Input(shape=(self._IMAGE_HEIGHT, self._IMAGE_WIDTH, 3))
        self.base_model = EfficientNetB0(
            include_top=True,
            weights="imagenet",
            input_tensor=inputs,
        )

    def base_predict_is_snake(self,
                              image: Image,
                              rescale: bool = False):
        image_resized = image.resize((self._IMAGE_WIDTH, self._IMAGE_HEIGHT))
        input_image_np = np.asarray(image_resized)
        input_image_np = input_image_np.reshape((1, self._IMAGE_WIDTH, self._IMAGE_HEIGHT, 3))
        if rescale:
            input_image_np *= 1. / 255
        predictions = self.base_model.predict(input_image_np)
        top_1_class = np.argmax(predictions)

        if 52 <= top_1_class <= 68:
            return True

        return False

    def predict(self,
                image: Image,
                rescale: bool = False,
                ):
        image_resized = image.resize((self._IMAGE_WIDTH, self._IMAGE_HEIGHT))
        input_image_np = np.asarray(image_resized)
        input_image_np = input_image_np.reshape((1, self._IMAGE_WIDTH, self._IMAGE_HEIGHT, 3))
        if rescale:
            input_image_np *= 1. / 255
        logging.debug(f"Resulting shape is {input_image_np.shape}")
        predictions = self.model.predict(input_image_np)

        return predictions

    def save_model(self, model_file_path: Path):
        self.model.save(model_file_path)

    def load_model(self, model_file_path: Path):
        self.model = load_model(model_file_path)
