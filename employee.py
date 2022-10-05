"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, base, hours, commission, commAmount, commType):
        self.name = name
        self.contract = contract
        self.base = base
        self.hours = hours
        self.commission = commission
        self.commAmount = commAmount
        self.commType = commType

    def get_pay(self):
        self.pay = 0
        if self.contract == 'monthly':
            self.pay = self.base
        elif self.contract == 'hourly':
            self.pay = self.base * self.hours

        self.pay = self.pay + (self.commission * self.commAmount)

        return self.pay

    def __str__(self):
        string = f'{self.name} works on a'

        if self.contract == 'monthly':
            string = f'{string} monthly salary of {self.base}'
        elif self.contract == 'hourly':
            string = f'{string} contract of {self.hours} hours at {self.base}/hour'

        if (self.commission != 0) and (self.commAmount != 0):
            if self.commType == 'contract':
                string = f'{string} and receives a commission for {self.commAmount} contract(s) at {self.commission}/contract'
            elif self.commType == 'bonus':
                string = f'{string} and receives a bonus commission of {self.commission}'

        string = f'{string}. Their total pay is {self.pay}.'

        return string

        # return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000, None, 0, 0, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100, 0, 0, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, None, 200, 4, 'contract')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150, 220, 3, 'contract')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, None, 1500, 1, 'bonus')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120, 600, 1, 'bonus')
