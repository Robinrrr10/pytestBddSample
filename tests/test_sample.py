from pytest_bdd import given, when, then, scenario

@scenario("../features/mytest.feature", "Sample test one")

def test_one():
    print("Hi Test")
    assert 1 == 1
    pass

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