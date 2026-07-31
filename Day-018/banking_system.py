class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("₹", amount, "Deposited")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("₹", amount, "Withdrawn")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance: ₹", self.__balance)

holder = input("Enter Account Holder Name: ")

balance = float(input("Enter Initial Balance: "))

account = BankAccount(holder, balance)

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        amount = float(input("Amount: "))
        account.deposit(amount)

    elif choice == "2":

        amount = float(input("Amount: "))
        account.withdraw(amount)

    elif choice == "3":

        account.show_balance()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")