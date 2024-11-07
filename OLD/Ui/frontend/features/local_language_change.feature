Feature: Local Language Change
  As a user
  I want to change the website language without a network connection
  So I can use the website in my preferred language

  Scenario: Changing language in offline mode
    Given the user is on the website without a network connection
    When the user selects a new language
    Then the website interface changes to display the selected language
