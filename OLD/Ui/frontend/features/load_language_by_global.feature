Feature: Automatic language change based on browser locale

    Background: The web application is configured to support multiple languages

    Scenario: A user visits the application with a French locale setting
        Given the user's browser is set to the "fr" language
        When the user accesses the web application
        Then the application displays in French

    Scenario: A user visits the application with an English locale setting
        Given the user's browser is set to the "en" language
        When the user accesses the web application
        Then the application displays in English
