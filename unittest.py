class BankAccount:
  def __init__(self, id):
    self.id=id
    self.balance=0

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      return True
    return False
  
  def deposit(self, amount):
    self.amount += amount
    return True
import unittest
class TestBank(unittest.TestCase):
  def test_insuffiecient_funds(self):
    a = BankAccount()
    a.deposit(100)
    outcome=a.withdraw(200)
    self.assertFalse(outcome)