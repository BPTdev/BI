Feature: Automatic Sending of Cached Images When Network is Recovered
  As a user
  I want cached images to be automatically sent once the network connection is restored
  So that I don't have to manually submit them

  Scenario: Automatic sending of images after network reconnection
    Given the user has images in cache waiting to be sent
    And the user regains network connection
    Then all cached images are automatically sent
