Feature: Asynchronous Operation and Image Storage on S3
  As a system
  I want to upload images to S3 and receive labels from AWS Rekognition asynchronously
  So as not to block other operations

  Scenario: Asynchronous storage and analysis
    Given an image is submitted for analysis
    When the image is uploaded to S3
    Then a request is sent to AWS Rekognition for analysis
    And this is done asynchronously to allow for other system interactions
