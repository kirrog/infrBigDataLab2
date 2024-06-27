import unittest

import pandas
import requests
from sklearn.pipeline import Pipeline

from main import app
from src.predict import Predictor
from src.preprocess import Preprocessor
from src.train import Trainer
from src.utils import split2x_y


class PredictionTest(unittest.TestCase):

    def test_type_of_answer(self):
        model = Predictor()
        floats = [[16.0, 15.0, 0.89, 6.0, 3.0, 4.0, 5.0]]
        y_result_data = model.predict_by_model(floats)
        self.assertEqual(len(y_result_data), 1)
        self.assertIsInstance(y_result_data[0], float)


class PreprocessingTest(unittest.TestCase):

    def test_preprocessor_creation(self):
        with self.assertRaises(Exception):
            Preprocessor(0.1, 0.1, 0.1)


class TrainerTest(unittest.TestCase):

    def test_pipeline_creation(self):
        pipeline = Trainer()
        self.assertIsInstance(pipeline.model, Pipeline)


class UtilsTest(unittest.TestCase):
    def test_splitting(self):
        dataframe_x = [[0.1] * 7, [0.2] * 7]
        data = {
            "Area": [0.1, 0.2],
            "Perimeter": [0.1, 0.2],
            "Compactness": [0.1, 0.2],
            "Kernel.Length": [0.1, 0.2],
            "Kernel.Width": [0.1, 0.2],
            "Asymmetry.Coeff": [0.1, 0.2],
            "Kernel.Groove": [0.1, 0.2],
            "Type": [1.0, 2.0]
        }
        dataframe = pandas.DataFrame(data)
        x, y = split2x_y(dataframe)
        self.assertEqual(x, dataframe_x)
        self.assertEqual(y, [1.0, 2.0])


class ApiTest(unittest.TestCase):
    def test_api_health(self):
        local_app = app
        local_app.config.update({"TESTING": True})
        test_client = app.test_client()

        r = test_client.get('http://localhost:5555/')
        result = r.text
        self.assertEqual(result, "Flask is running!")
