Feature: Addition of two numbers
  Scenario: Test1
    Given two numbers 1 and 4
    When they are added
    Then the result should be 5

  Scenario: Test2
    Given two numbers -10 and 3
    When they are added
    Then the result should be -7

  Scenario: Test3
    Given two numbers 5 and 5
    When they are added
    Then the result should be 10