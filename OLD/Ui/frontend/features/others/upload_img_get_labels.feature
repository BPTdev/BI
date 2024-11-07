Feature: Scenario end to end
    As a user
    I want to upload an image and get labels from aws
    So I can know what is in the image

    Scenario: Upload image to get labels
    Given the user is on the website
    When the user upload an image
    And the user set the max_label and min_confidence params
    Then the web site returns labels
    And disply labels in the page