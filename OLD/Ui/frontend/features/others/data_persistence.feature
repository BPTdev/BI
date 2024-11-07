Feature: Data Persistence After Page Reload
  As a user
  I want my data (cached images, selected language) to be preserved after a page reload
  So that I do not lose my ongoing work

  Scenario: Data is preserved after reloading
    Given the user has cached images and a selected language
    When the user reloads the page
    Then the cached images and the selected language are preserved
