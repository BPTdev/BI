Feature: Drag and Drop Box
  As a user
  I want to be able to drag and drop images into the designated area
  So that they can be sent for analysis

  Scenario: Successfully dragging and dropping a valid image
    Given the user is on the image submission page
    When the user drags and drops a valid image into the drag and drop area
    Then the image is displayed in the preview area
    And it is added to the list of images pending submission
