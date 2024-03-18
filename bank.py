class Bank:
  def __init__(self, name, acc_num):
    self.name=name
    self.acc_num=acc_num
  
class fixed_acc(Bank):
  def __init__(self,name, acc_num, acc_balance,amount):
    self.name=name
    self.acc_num=acc_num
    self.acc_balance=acc_balance
    self.amount=amount
  def newBalance(self):
    total_balance = self.acc_balance + self.amount
    return(total_balance)

class dormantAcc(fixed_acc):
  def __init__(self,name,acc_num,acc_balance,amount):
    self.name=name
    self.acc_num=acc_num
    self.acc_balance=acc_balance
    self.amount=amount
  def isDormant(self):
    total= self.acc_balance + self.amount
    if (total < 30000):
      return("dormant.")
    else:
      return('active.')
  
class currentAcc(dormantAcc, fixed_acc):
  def __init__(self,name,acc_num,acc_balance, amount):
    self.name=name
    self.acc_num=acc_num
    self.acc_balance=acc_balance
    self.amount=amount

class juniorAccount(fixed_acc):
  def __init__(self,name, acc_num, acc_balance, amount):
    self.name=name
    self.acc_num=acc_num
    self.acc_balance=acc_balance
    self.amount=amount

checkIn1=currentAcc("Ian Muriuki","0650182000829", 45000, 1500)
jACC1 = juniorAccount("Essy Kitchens","0378593848", 0, 4500)
print(f'New balance after depositing {jACC1.amount} is {jACC1.newBalance()}')
print(f'Current account balance is {checkIn1.acc_balance}')
print(f'This current account is {checkIn1.isDormant()}') 