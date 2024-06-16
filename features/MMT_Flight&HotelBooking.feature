Feature: Round Trip Flight Booking
  This is MakeMyTrip Flight Booking For RoundTrip using Python With Selenium.

  @Flight
  Scenario: RoundTrip flight booking
    Given I am on flight home page
    When I login to the page
    And I select destinations for round trip
    And I choose departure and return date
    And I choose my flights
    And I provide passenger detail
    Then I get to the payment gateway

  @Hotel
  Scenario: Hotel Booking
    Given I am on hotel home page
    When I login to the page
    And I select hotel for destination city
    And I select checkin and checkout date
    And I choose preferred hotel
    And I provide booking details
    Then I get on payment page