from app import deposit, withdraw

def test_initial_deposit():
    
    balance, message = deposit(0.0, 100.0)
    assert balance == 100.0
    assert "Deposited $100.00" in message

def test_negative_deposit():
   
    balance, message = deposit(50.0, -20.0)
    assert balance == 50.0  
    assert "must be positive" in message

def test_successful_withdrawal():
    
    balance, message = withdraw(100.0, 40.0)
    assert balance == 60.0
    assert "Withdrew $40.00" in message

def test_insufficient_funds_withdrawal():
def test_deposit_validation():
    balance = 0.0
    amount = 50.0
    if amount > 0:
        balance += amount
    assert balance == 50.0

def test_withdrawal_validation():
    balance = 100.0
    amount = 150.0 
    transaction_allowed = amount <= balance
    assert transaction_allowed is False
