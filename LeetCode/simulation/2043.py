class Bank:
    balance = []

    def __init__(self, balance: List[int]):
        self.balance = balance

    
    # 계좌1 -> 계좌2
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (1 <= account1 <= len(self.balance)) and (1 <= account2 <= len(self.balance)) and (money <= self.balance[account1 - 1]):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
        else:
            return False
        return True
    
    
    # 입금
    def deposit(self, account: int, money: int) -> bool:
        if (1 <= account <= len(self.balance)):
            self.balance[account - 1] += money
        else:
            return False
        return True
    

    # 출금
    def withdraw(self, account: int, money: int) -> bool:
        if (1 <= account <= len(self.balance)) and (self.balance[account - 1] >= money):
            self.balance[account - 1] -= money
        else:
            return False
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
