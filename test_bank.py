import pytest
from bank import BankAccount, InsufficientFund
import sys

# Fixtures run before the test where we call it
# Fixture scope can be changed, bydefault its scope is function
# we can change scope of fixture to class, module, package or session

# when we give module scope this will run only once for the module
# @pytest.fixture(scope="module")
# def zero_bank_account():
#     return BankAccount(0)

@pytest.fixture
def zero_bank_account():
    return BankAccount(0)

@pytest.fixture
def bank_account():
    return BankAccount(50)


def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_default_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == 100

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 20

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

# ids will tag names to each test case which is parameterized
@pytest.mark.parametrize(
    "deposited, withdraw, expected",
    [
        (10, 10, 0),
        (100, 0, 100),
        (10, 6, 4),
        (0, 0, 0),
    ],
    ids=[
            "deposit and withdraw", 
            "only deposit",
            "deposit, withdraw and expected",
            "all"
        ]
    )
def test_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected

# Write seperate case to test exception
# Always expect Exact Exception, 
# If we catching generic Exception then we cannot differentiate 
# between errors like ZeroDivisionError, InsufficientError
def test_insufficient_funds(zero_bank_account):
    with pytest.raises(InsufficientFund):
        zero_bank_account.withdraw(10)
        
def test_insufficient_funds_message(zero_bank_account):
    with pytest.raises(InsufficientFund) as e:
        zero_bank_account.withdraw(10)
    assert str(e.value) == "Insufficient balance."
    
def test_insufficient_funds_message_with_match(zero_bank_account):
    with pytest.raises(InsufficientFund, match="Insufficient balance."):
        zero_bank_account.withdraw(10)

# we can skip test when we add skip decorator
@pytest.mark.skip(reason="Skipped as function is not implemented")
def test_skip(zero_bank_account):
    with pytest.raises(InsufficientFund, match="Insufficient balance."):
        zero_bank_account.withdraw(10)


# we can skip test when we add skip when condition matches
@pytest.mark.skipif(sys.version_info > (3,7),reason="Skipped as python version is > 3.7")
def test_skip_with_reason(zero_bank_account):
    with pytest.raises(InsufficientFund, match="Insufficient balance."):
        zero_bank_account.withdraw(10)

# Here we assume that when condition is met this test is expected to fail,
# like few commands does not work on windows
@pytest.mark.xfail(sys.platform == "darwin",reason="This test will fail on MacOS, so dont run on macOS")
def test_fail(zero_bank_account):
    with pytest.raises(InsufficientFund, match="Insufficient balance."):
        zero_bank_account.withdraw(10)
