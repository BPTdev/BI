
Feature: Display Detected Labels with Confidence Levels

  Background: The user has uploaded an image for analysis

  Scenario: Displaying the list of detected labels with confidence levels
    Given the user has successfully uploaded an image
    When the system processes the image and detects labels
    Then the user is presented with a list of detected labels
    And each label is accompanied by its level of confidence
