from .ILabelDetector import ILabelDetector
from .RekognitionClient import RekognitionClient


class AwsLabelDetectorImpl(ILabelDetector):
    def __init__(self):
        self.client = RekognitionClient()

    @staticmethod
    def analyze(remote_full_path: str, max_labels: int = 5, min_confidence_level: float = 90) -> str:
        # Create a Rekognition client instance
        client = RekognitionClient()

        # Set parameters using methods
        client.set_min_confidence(min_confidence_level)
        client.set_max_labels(max_labels)

        response = client.detect_labels(remote_full_path)
        return response
