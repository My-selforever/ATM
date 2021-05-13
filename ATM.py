class atm:
    def __init__(self,pin,balance,user):
        self.pin = pin
        self.balance = balance
        self.user = user

    def Withdraw(self):
        amount = print(input("How much?:"))
        if(amount<=self.balance):
            self.balance = self.balance-amount
            print("Successfully Withdrawed",amount,"rupees")
        elif(amount>self.balance):
            print("insuffiecent Funds")

    def Deposit(self):
        amount = print(input("How much?: "))
        self.balance = self.balance+amount
        print("Successfully Deposited",amount,"rupees")

    def ChangePin(self):
        pin = print(input("Current Pin: "))
        if(pin==self.pin):
            newPin = print(input("New Pin: "))
            self.pin = pin
            print("Pin CHanged Successfully")
        else:
            print("Incorrect Pin")


name = print(input("What is your name?: "))
pin = print(input("What is your pin?: "))
balance = print(input("What is your balance?: "))
user = atm(pin,balance,name)