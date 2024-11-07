Feature: Network Error Management
  As a user
  I want to be informed when there are network issues affecting data sending or receiving
  So that I can take appropriate action

  Scenario: Displaying an error during a network disconnection
    Given the user attempts to send an image
    When there is a network disconnection
    Then an error message is displayed to the user informing them of the problem
