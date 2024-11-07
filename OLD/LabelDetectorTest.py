import unittest
import os
from LabelDetector.AwsLabelDetectorImpl import AwsLabelDetectorImpl


class TestLabelDetector(unittest.TestCase):
    def setUp(self):
        # Définissez vos variables ici
        self.localFile = "2.png"
        self.remote_full_url = "https://www.admin.ch/gov/de/start/departemente/departement-fuer-auswaertige-angelegenheiten-eda/_jcr_content/par/image/image.imagespooler.jpg/1611330706364/Cassis.jpg"
        self.label_detector = AwsLabelDetectorImpl()  # Remplacez par votre classe réelle
        return super().setUp()

    def test_analyze_local_file_with_default_values_image_analyzed(self):
        # Given
        self.assertTrue(os.path.exists(self.localFile))  # Assurez-vous que localFile existe

        # When
        response = self.label_detector.analyze(self.localFile)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response['Labels']) <= 10)
        for metric in response['Labels']:
            self.assertTrue(metric['Confidence'] >= 90)

    def test_analyze_remote_image_with_default_values_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible

        # When
        response = self.label_detector.analyze(self.remote_full_url)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response['Labels']) <= 10)
        for metric in response['Labels']:
            self.assertTrue(metric['Confidence'] >= 90)

    def test_analyze_remote_image_with_custom_max_label_value_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible
        max_labels = 5

        # When
        response = self.label_detector.analyze(self.remote_full_url, max_labels)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response['Labels']) <= max_labels)
        for metric in response['Labels']:
            self.assertTrue(metric['Confidence'] >= 90)

    def test_analyze_remote_image_with_custom_min_confidence_level_value_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible
        min_confidence_level = 60

        # When
        response = self.label_detector.analyze(self.remote_full_url, min_confidence_level= min_confidence_level)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)
        
        # Then
        
        self.assertTrue(len(response['Labels']) <= 10)
        for metric in response['Labels']:
            self.assertTrue(metric['Confidence'] >= min_confidence_level)

    def test_analyze_remote_image_with_custom_values_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible
        max_labels = 5
        min_confidence_level = 60

        # When
        response = self.label_detector.analyze(self.remote_full_url, max_labels, min_confidence_level)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response['Labels']) <= max_labels)
        for metric in response['Labels']:
            self.assertTrue(metric['Confidence'] >= min_confidence_level)

if __name__ == '__main__':
    unittest.main()
