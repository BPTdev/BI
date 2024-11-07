import os
import unittest

from dotenv import load_dotenv
import requests
from DataObject.AwsDataObjectImpl import AwsDataObjectImpl, ObjectNotFoundException


class DataObjectTests(unittest.TestCase):
    # Variables de test
    load_dotenv()

    # Retrieve credentials from environment variables
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region_name = os.getenv('AWS_REGION')

    local_file = "1.png"
    destination_folder = "/tmp/"
    bucket_uri = "python.cloud.aws.edu"

    object_uri = bucket_uri+"/"+local_file

    object_uri_with_subfolder = bucket_uri+destination_folder+local_file

    def setUp(self):
        # Initialisation de votre data object (à remplacer par la logique réelle)
        self.data_object = AwsDataObjectImpl()

    def tearDown(self):
        # Nettoyage de votre data object (à remplacer par la logique réelle)
        self.data_object.remove(self.object_uri, True)

        # Remove the downloaded file
        if os.path.exists("downloaded_file.png"):
            os.remove("downloaded_file.png")

    # Test cases for DoesExist
    def test_does_exist_existing_bucket_bucket_exists(self):
        # Given
        # The bucket is always available

        # When

        # Then
        self.assertTrue(self.data_object.does_exist(self.bucket_uri))

    def test_does_exist_existing_object_object_exists(self):
        # Given
        # The bucket is always available
        self.data_object.upload(self.local_file, self.object_uri)

        # When
        # Check the assertion

        # Then
        self.assertTrue(self.data_object.does_exist(self.bucket_uri))

    def test_does_exist_missing_object_object_not_exists(self):
        # Given
        # The bucket is always available
        # The bucket is empty (or does not contain the expected object)
        self.data_object.remove(self.object_uri)

        # When
        # Check the assertion

        # Then
        self.assertFalse(self.data_object.does_exist(self.object_uri))

    # Test case for Upload
    def test_upload_bucket_and_local_file_are_available_new_object_created_on_bucket(self):
        # Given
        self.assertTrue(self.data_object.does_exist(self.bucket_uri))
        self.assertFalse(self.data_object.does_exist(self.object_uri))

        # When
        self.data_object.upload(self.local_file, self.object_uri)

        # Then
        self.assertTrue(self.data_object.does_exist(self.object_uri))

    # It is the client's responsibility to verify (precondition) that the local file is accessible before attempting to upload.

    # Test cases for Download
    def test_download_object_and_local_path_available_object_downloaded(self):
        # Given
        self.data_object.upload(self.local_file, self.object_uri)
        self.assertTrue(self.data_object.does_exist(self.object_uri))
        self.assertFalse(os.path.exists("downloaded_file.png"))

        # When
        self.data_object.download(self.object_uri, "downloaded_file.png")

        # Then
        self.assertTrue(os.path.exists(self.local_file))

    def test_download_object_missing_throw_exception(self):
        # Given
        self.assertFalse(self.data_object.does_exist(self.bucket_uri+'/'+'missing_object.png'))
        self.assertFalse(os.path.exists("downloaded_file.png"))

        # When
        with self.assertRaises(ObjectNotFoundException):
            self.data_object.download(self.object_uri, "downloaded_file.png")

        # Then
        # Exception thrown

    # Test cases for Publish
    def test_publish_object_exists_public_url_created(self):
        # Given
        self.assertTrue(self.data_object.does_exist(self.object_uri))
        self.assertTrue(os.path.exists(self.destination_folder))

        # When
        presigned_url = self.data_object.publish(self.object_uri)
        # TODO: Download file using wget or another method that does not need our project library

        response = requests.get(presigned_url)

        if response.status_code == 200:
            with open(self.local_file, 'wb') as local_file:
                local_file.write(response.content)


        # Then
        self.assertTrue(os.path.exists(self.local_file))

    def test_publish_object_missing_throw_exception(self):
        # Given
        self.assertFalse(self.data_object.does_exist(self.object_uri))

        # When
        with self.assertRaises(ObjectNotFoundException):
            self.data_object.publish(self.object_uri)

        # Then
        # Exception thrown

    # Test cases for Remove
    def test_remove_object_present_no_folder_object_removed(self):
        # Given
        self.assertTrue(self.data_object.does_exist(self.object_uri))

        # When
        self.data_object.remove(self.object_uri)

        # Then
        self.assertFalse(self.data_object.does_exist(self.bucket_uri))

    def test_remove_object_and_folder_present_object_removed(self):
        # Given
        # The bucket contains objects at the root level as well as in subfolders
        # Sample: mybucket.com/myobject     # myObject is a folder
        #         mybucket.com/myobject/myObjectInSubfolder
        
        self.assertTrue(self.data_object.does_exist(self.object_uri))
        self.assertTrue(self.data_object.does_exist(self.object_uri_with_subfolder))

        # When
        self.data_object.remove(self.object_uri, True)

        # Then
        self.assertFalse(self.data_object.does_exist(self.object_uri))

if __name__ == '__main__':
    unittest.main()
