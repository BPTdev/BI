Feature: Dynamic Display of Pending Requests
  As a user
  I want to see the number of pending requests (images in cache to be sent)
  So I know the status of my submissions

  Scenario: Displaying the number of pending requests
    Given the user has several images pending submission
    When a new image is added to the list
    Then the displayed number of pending requests is incremented
