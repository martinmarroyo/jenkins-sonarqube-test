import pytest
from bank import Account

@pytest.fixture(scope="function")
def account():
    acct = Account(1, 1500)
    return acct


def test_credit_acct(account):
    acct = account
    acct.credit(1500)
    assert acct.balance == 3000


def test_debit_acct(account):
    acct = account
    acct.debit(1200)
    assert acct.balance == 300


def test_get_balance(account):
    acct = account
    expected_balance = 1500
    result_balance = acct.get_balance()
    assert expected_balance == result_balance


def test_get_acct_number(account):
    acct = account
    assert acct.get_acct_number() == 2