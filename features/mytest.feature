Feature: Sample test for pytest bdd

    Scenario: Sample test one
        Given current balance was 10
        When deduct 7 rupees
        Then balance should be 3 rupees
    
    Scenario: Sample test two
        Given current balance was 10
        When deduct 7 rupees
        Then balance should be 3 rupees