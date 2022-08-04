import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s - %(message)s",
    stream=sys.stdout 
)
class Account():
    def __init__(self, id:int, balance:float = 0.0):
        self.id = id
        self.balance = round(balance, 2)
        logging.info(f"New account:\nID: {self.id}\nBalance: ${self.balance}")

    def credit(self, amount:float):
        logging.info(f"Transaction (CREDIT): + ${amount}")
        self.balance += round(amount, 2)
        logging.info(f"Account balance: ${self.balance}")

    def debit(self, amount:float):
        logging.info(f"Transaction (DEBIT): - ${amount}")
        self.balance -= round(amount, 2)
        logging.info(f"Account balance: ${self.balance}")

    def get_balance(self):
        logging.info(f"Account balance: ${self.balance}")
        return self.balance

    def get_acct_number(self):
        logging.info(f"Account Number: {self.id}")
        return self.id
