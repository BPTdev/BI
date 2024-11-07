Feature: Dynamic Display Without Page Reload
  As a user
  I want content updates to be displayed dynamically without reloading the page
  So I can see new images and information without interruption

  Scenario: Adding a new image without reloading the page
    Given the user is on the main page
    When the user adds a new image via drag and drop
    Then the image is instantly displayed on the page without reloading
