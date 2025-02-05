"""
class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def display_customer(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Phone No.: {self.phone_number}")

class Depositor(Customer):
    def __init__(self, name, phone_number, acc_no, balance):
        super().__init__(name, phone_number)
        self.acc_no = acc_no
        self.balance = balance

    def display_depositor(self):
        self.display_customer()
        print(f"Customer A/C No.: {self.acc_no}")
        print(f"Balance: {self.balance}")

class Borrower(Depositor):
    def __init__(self, name, phone_number, acc_no, balance, loan_no, loan_amt):
        super().__init__(name, phone_number, acc_no, balance)
        self.loan_no = loan_no
        self.loan_amt = loan_amt

    def display_borrower(self):
        self.display_depositor()
        print(f"Loan No.: {self.loan_no}")
        print(f"Loan Amount: {self.loan_amt}")
        print("------------------------------------------------------")

# Function to take input for 'n' customers
def main():
    customers = []
    n = int(input("Enter number of customer details you want to add: "))

    for i in range(n):
        print("\nEnter details for customer", i + 1)
        name = input("Enter Customer Name: ")
        phone_number = input("Enter Customer Phone.No: ")
        acc_no = input("Enter Customer A/C No: ")
        balance = float(input("Enter Balance: "))
        loan_no = input("Enter Loan Number: ")
        loan_amt = float(input("Enter Loan Amount: "))

        customer = Borrower(name, phone_number, acc_no, balance, loan_no, loan_amt)
        customers.append(customer)
        print("*" * 50)

    print("\nDetails Of Customers:")
    for customer in customers:
        customer.display_borrower()

if __name__ == "__main__":
    main()
"""
nums = list(map(int, input("Enter the binary array elements (space-separated): ").split()))
prefix_sum = {0: -1}  # Dictionary to store first occurrence of cumulative sum
sum_so_far = 0
max_length = 0
for i in range(len(nums)):
    # Convert 0 to -1 for balance calculation
    if nums[i] == 0:
        sum_so_far -= 1
    else:
        sum_so_far += 1
    if sum_so_far in prefix_sum:
        max_length = max(max_length, i - prefix_sum[sum_so_far])
    else:
        prefix_sum[sum_so_far] = i  # Store first occurrence of this sum
print("Length of the longest good subarray:", max_length)
