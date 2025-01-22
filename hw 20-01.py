class BankAccount:
    def __init__(self,acc_no=None,balance=0):
        self.__acc_no=acc_no
        self.__balance=balance
    def set_acc_no(self):
        self.__acc_no=input("Enter account number:")
        while True:
            try:
                self.__balance = float(input("Enter initial balance: "))
                if self.__balance < 0:
                    print("Initial balance cannot be negative. Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    def deposit(self):
        while True:
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    self.__balance += amount
                    print(f"Deposited: {amount}")
                    break
                else:
                    print("Deposit amount must be positive. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def withdraw(self):
        while True:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if 0 < amount <= self.__balance:
                    self.__balance -= amount
                    print(f"Withdrew: {amount}")
                    break
                else:
                    print("Insufficient balance or invalid amount. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    def add_interest(self):
        while True:
            try:
                rate = float(input("Enter interest rate (as a percentage): "))
                if rate > 0:
                    interest = self.__balance * (rate / 100)
                    self.__balance += interest
                    print(f"Added interest: {interest:.2f}")
                    break
                else:
                    print("Interest rate must be positive. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    def display_details(self):
        print("\nAccount Details")
        print(f"Account Number:{self.__acc_no}")
        print(f"Balance:{self.__balance:.2f}")
def main():
    account = BankAccount()
    account.set_acc_no()

    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Add Interest")
        print("4. Display Account Details")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account.deposit()
        elif choice == "2":
            account.withdraw()
        elif choice == "3":
            account.add_interest()
        elif choice == "4":
            account.display_details()
        elif choice == "5":
            print("Exiting. Thank you for using the BankAccount system!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
