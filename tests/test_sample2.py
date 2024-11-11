from pytest_bdd import given, when, then, scenarios

#scenarios("../features/mytest.feature") #to run multiple scenarios in single file
scenarios("../features/") #to run multiple scenarios in multiple files

@given("current balance was 10")
def balance():
    print("Current balance is get called")

@when("deduct 7 rupees")
def deductingAmount():
    print("Amount was deducted")

@then("balance should be 3 rupees")
def balanceAfterDeduction():
    print("Balance after deduction was called")
    assert 5 == 5

@then("Show price")
def balanceAfterDeduction():
    print("Showing price is 5")