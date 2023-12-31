import boto3
import json


class RekognitionClient:
    def __init__(self, credentials_file):
        # Load credentials from JSON file
        with open(credentials_file, "r") as file:
            credentials = json.load(file)

        # Set up AWS session and create a Rekognition client
        self.session = boto3.Session(
            aws_access_key_id=credentials["aws_access_key_id"],
            aws_secret_access_key=credentials["aws_secret_access_key"],
            region_name=credentials["region_name"],
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

    def detect_labels(self, image_path, simplified=True):
        # Print current parameters
        print(f"Current Parameters: Max Labels: {self.max_labels}, Min Confidence: {self.min_confidence}, Features: {self.features}, Settings: {self.settings}")

        # Open the image file
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        if simplified:
            features = ["GENERAL_LABELS"]
        else:
            features = ["GENERAL_LABELS", "IMAGE_PROPERTIES"]

        # Call Amazon Rekognition to detect labels in the image
        response = self.rekognition.detect_labels(
            Image={"Bytes": image_bytes},
            MaxLabels=self.max_labels,
            MinConfidence=self.min_confidence,
            Features=features,
            Settings=self.settings,
        )

        # Return the detected labels
        return response
