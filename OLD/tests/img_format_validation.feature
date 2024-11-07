Feature: Image Format Validation
  As a system
  I want to only accept supported image formats for sending and analysis
  So as to avoid processing errors

  Scenario: Rejecting unsupported image formats
    Given a user attempts to send an image in an unsupported format
    When the image is submitted
    Then it is rejected by the system
    And an error message is displayed to the user
