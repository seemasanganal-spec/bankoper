def bankoper(balance, deposit, withdraw):
    totalBalance = balance + deposit
    updatedBalance = totalBalance - withdraw

    return totalBalance, updatedBalance


if __name__ == "__main__":
    balance = 1000000
    deposit = 12300
    withdraw = 1234

    totalBalance, updatedBalance = bankoper(balance, deposit, withdraw)

    print("Total Balance after deposit:", totalBalance)
    print("Updated Balance after withdraw:", updatedBalance)