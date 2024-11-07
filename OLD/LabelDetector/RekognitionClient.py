import os
import boto3
from dotenv import load_dotenv
import requests
from io import BytesIO


class RekognitionClient:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Set up AWS session and create a Rekognition client
        self.session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION"),
        )
        self.rekognition = self.session.client("rekognition")

        # Initialize default values
        self.max_labels = 10
        self.min_confidence = 70
        self.features = ["GENERAL_LABELS"]
        self.settings = {
            "GeneralLabels": {
                "LabelInclusionFilters": [],
                "LabelExclusionFilters": [],
                "LabelCategoryInclusionFilters": [],
                "LabelCategoryExclusionFilters": [],
            },
        }

    def set_max_labels(self, max_labels):
        self.max_labels = max_labels

    def set_min_confidence(self, min_confidence):
        self.min_confidence = min_confidence

    def add_label_inclusion(self, label):
        self.settings["GeneralLabels"]["LabelInclusionFilters"].append(label)

    def add_label_exclusion(self, label):
        self.settings["GeneralLabels"]["LabelExclusionFilters"].append(label)

    def add_label_category_inclusion(self, label):
        self.settings["GeneralLabels"]["LabelCategoryInclusionFilters"].append(label)

    def add_label_category_exclusion(self, label):
        self.settings["GeneralLabels"]["LabelCategoryExclusionFilters"].append(label)

    # You can add similar methods for category inclusion and exclusion

    def detect_labels(self, image_source, simplified=True):
        if image_source.lower().startswith("http://") or image_source.lower().startswith("https://"):
            response = requests.get(image_source)
            if response.status_code == 200:
                image_bytes = BytesIO(response.content)
            else:
                raise Exception(f"Failed to download image from URL: {image_source}")
        else:
            with open(image_source, "rb") as image_file:
                image_bytes = BytesIO(image_file.read())

        if simplified:
            features = ["GENERAL_LABELS"]
        else:
            features = ["GENERAL_LABELS", "IMAGE_PROPERTIES"]

        response = self.rekognition.detect_labels(
            Image={"Bytes": image_bytes.getvalue()},
            MaxLabels=self.max_labels,
            MinConfidence=self.min_confidence,
            Features=features,
            Settings=self.settings,
        )

        return response
