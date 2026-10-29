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
    
    balance, message = withdraw(50.0, 100.0)
    assert balance == 50.0
    assert "Insufficient funds" in message

def test_negative_withdrawal():
   
    balance, message = withdraw(50.0, -10.0)
    assert balance == 50.0
    assert "must be positive" in message
