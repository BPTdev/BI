Feature: Queue Management for Successive Requests
  As a system
  I want to manage a queue of requests sent to AWS Rekognition
  So that each request is processed in order without being lost

  Scenario: Processing requests in the order they were received
    Given several image analysis requests are sent almost simultaneously
    When they are received by the system
    Then they are added to a queue
    And processed in the order they were received
