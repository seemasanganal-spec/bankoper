from bankoper import bankoper

def test_deposit():
    totalBalance, updatedBalance = bankoper(200000, 30000, 0)
    assert totalBalance == 230000
    assert updatedBalance == 230000

def test_withdraw():
    totalBalance, updatedBalance = bankoper(100000, 40000, 10000)
    assert totalBalance == 140000
    assert updatedBalance == 130000

def test_anyamount():
    totalBalance, updatedBalance = bankoper(150000, 0, 150000)
    assert totalBalance == 150000
    assert updatedBalance == 0