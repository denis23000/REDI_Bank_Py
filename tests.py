import pytest
from class_bank_account import BankAccount



test_account = BankAccount(name="account_1", account_nr=123456789, balance=100)

isinstance(test_account, BankAccount)
if isinstance(test_account, BankAccount):
    print('yes, it is a bank account')
else:
    print('it is not a bank account')


def test_only_positive_amount():



    with pytest.raises(ValueError):
        test_account.deposit(-100)
    with pytest.raises(ValueError):
        test_account.withdraw(-100)


def test_no_strings_allowed():



    with pytest.raises(ValueError):
        test_account.deposit('Jimi')
    with pytest.raises(ValueError):
        test_account.withdraw('Jimi')

def test_no_negavtive_balance_allowed():



    with pytest.raises(ValueError):
        test_account.withdraw(5000)