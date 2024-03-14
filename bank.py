class Bank:
  def __init__(self, name, acc_num):
    self.name=name
    self.acc_num=acc_num
  
class deposit_acc(Bank):
  def __init__(self,name, acc_num, acc_balance,amount):
    self.name=name
    self.acc_num=acc_num
    self.acc_balance=acc_balance
    self.amount=amount
  def newBalance(self):
    total_balance = self.acc_balance + self.amount
    print(total_balance)

class dormantAcc(deposit_acc):
  def __init__(self,name,acc_num,acc_balance,amount):
    self.name=name
    self.acc_num=acc_num
    self.acc_balance=acc_balance
    self.amount=amount
  def isDormant(self):
    total= self.acc_balance + self.amount
    if (total < 30000):
      print("Account is dormant.")
    else:
      print("Account is active.")
  
class activeAcc(dormantAcc, deposit_acc):
  def _init_(self,name,acc_num,acc_balance, amount):
    self.name=name
    self.acc_num=acc_num
    self.acc_balance=acc_balance
    self.amount=amount

checkIn1 = activeAcc("Ian",34562,1357.98,450000)
checkIn1.newBalance()
checkIn1.isDormant()