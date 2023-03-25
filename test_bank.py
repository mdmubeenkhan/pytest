import pytest
from bank import BankAccount, InsufficientFund

# Fixtures run before the test where we call it
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


@pytest.mark.parametrize(
    "deposited, withdraw, expected",
    [
        (10, 10, 0),
        (100, 0, 100),
        (10, 6, 4),
        (0, 0, 0)
    ])
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