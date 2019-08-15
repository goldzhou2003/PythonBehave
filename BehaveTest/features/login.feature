Feature: login test

  @test
  Scenario Outline: people login
    Given login page open
    """
    this is text of given
    """
    When input user name <username> and pass <pw>
    Then login into page

    Examples: login info
    | username | pw |
    | test | 1234   |
  # -- AFTER-SCENARIO: Cleanup fixture.test.fixture

#    | zhou | 2345   |

#  Scenario: tttt
#    Given had something
#    Then this is a
#
#  Scenario: aaaa
#    Given had something else
#    Then this is b

#  Scenario: look up a book
#    Given I search for a valid book
#    Then the result page will include "success"
#
#  Scenario: look up an invalid book
#    Given I search for a invalid book
#    Then the result page will include "failure"