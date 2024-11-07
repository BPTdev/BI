
Feature: Parameters Adjustment for Label Detection

  Background: The user is on the parameters adjustment zone

  Scenario: Adjusting parameters for label detection
    Given the user sets the "amount of labels" to display to "5"
    And the user sets the "level of confidence" threshold to "80%"
    And the user submits the parameters
    Then the system updates the displayed labels to match the new parameters
    And only labels with a confidence level of "80%" or higher are displayed
    And no more than "5" labels are displayed
