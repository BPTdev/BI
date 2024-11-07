import os
from dotenv import load_dotenv
from .IDataObject import IDataObject
import boto3
import mimetypes
import magic
import requests


class AwsDataObjectImpl(IDataObject):
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Retrieve credentials from environment variables
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        region_name = os.getenv("AWS_REGION")

        # Set up AWS session and create an S3 client
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )
        self.s3 = self.session.client("s3")

    def does_exist(self, remote_file_path: str) -> bool:
        if "/" not in remote_file_path:
            # If no '/' is present, assume it's a bucket name and check its existence
            try:
                self.s3.head_bucket(Bucket=remote_file_path)
                return True
            except boto3.exceptions.botocore.exceptions.ClientError as e:
                if e.response["Error"]["Code"] == "404":
                    return False
                else:
                    raise
        else:
            # If '/' is present, split into bucket name and object name
            bucket_name, object_name = remote_file_path.split("/", 1)
            try:
                self.s3.head_object(Bucket=bucket_name, Key=object_name)
                return True
            except boto3.exceptions.botocore.exceptions.ClientError as e:
                if e.response["Error"]["Code"] == "404":
                    return False
                else:
                    raise

    def upload(self, file_path: str, remote_file_path: str) -> None:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        bucket_name, object_name = remote_file_path.split("/", 1)
        self.s3.upload_file(file_path, bucket_name, object_name)

    def download(self, remote_file_path: str, local_file_path: str) -> None:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        bucket_name, object_name = remote_file_path.split("/", 1)
        if not self.does_exist(remote_file_path):
            raise ObjectNotFoundException()
        self.s3.download_file(bucket_name, object_name, local_file_path)

    def publish(self, remote_file_path: str, expiration_time: int = 90) -> str:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        bucket_name, object_name = remote_file_path.split("/", 1)
        response = self.s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_name},
            ExpiresIn=expiration_time * 60,
        )
        return response

    def remove(self, remote_file_path: str, recursive: bool = False) -> None:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        bucket_name, object_name = remote_file_path.split("/", 1)

        if recursive:
            bucket = self.session.resource("s3").Bucket(bucket_name)
            bucket.objects.filter(Prefix=object_name).delete()
        else:
            self.s3.delete_object(Bucket=bucket_name, Key=object_name)

    def api_call(self, bucket, image_path, remote_full_path):
        file_name_with_extension = None
        if image_path.lower().startswith("http://") or image_path.lower().startswith("https://"):
            response = requests.get(image_path)
            if response.status_code == 200:
                file_type = magic.from_buffer(response.content, mime=True)
                extension = mimetypes.guess_extension(file_type)

                if not extension:
                    raise ValueError("Could not determine the file extension")

                file_name_with_extension = 'temp_image' + extension

                with open(file_name_with_extension, 'wb') as file:
                    file.write(response.content)
                image_path = file_name_with_extension

                remote_full_path = bucket + '/' + file_name_with_extension
            else:
                raise Exception(f"Failed to download image from URL: {image_path}")

        if not self.does_exist(bucket):
            pass
        if not self.does_exist(remote_full_path):
            self.upload(image_path, remote_full_path)
        else:
            self.upload(image_path, remote_full_path)

        if file_name_with_extension and os.path.exists(file_name_with_extension):
            os.remove(file_name_with_extension)
        if file_name_with_extension:
            return bucket + '/' + file_name_with_extension
        else:
            return remote_full_path


class AwsDataObjectImplException(Exception):
    pass


class ObjectAlreadyExistsException(AwsDataObjectImplException):
    def __init__(self, message="The specified object already exists in S3"):
        self.message = message
        super().__init__(self.message)


class ObjectNotFoundException(AwsDataObjectImplException):
    def __init__(self, message="The specified object was not found in S3"):
        self.message = message
        super().__init__(self.message)


class NotEmptyObjectException(AwsDataObjectImplException):
    def __init__(self, message="The specified object is not empty"):
        self.message = message
        super().__init__(self.message)
