class BookStore:
    def __init__(self):
        self.discounts = {
            range(1, 101): 50,
            range(101, 301): 30,
            range(301, 401): 20,
            range(401, 501): 10,}
    def get_discount(self, customer_id):
        for key, discount in self.discounts.items():
            if customer_id in key:
                return discount
        return 0  # No discount for customer IDs > 500    
    def calculate_discounted_price(self, price, discount):
        return price - (price * discount / 100)
    def process_customer(self):
        while True:
            try:
                book_name = input("Enter your Book Name: ")
                if not book_name.strip():
                    raise ValueError("Book name cannot be empty.")
                customer_id = int(input("Enter your Customer ID: "))
                if customer_id <= 0:
                    raise ValueError("Customer ID must be a positive integer.")
                price = float(input("Enter the Price of the Book: "))
                if price <= 0:
                    raise ValueError("Price must be a positive number.")
                discount = self.get_discount(customer_id)
                discounted_price = self.calculate_discounted_price(price, discount)
                print(f"Price of the Book is {price} MRP")
                print(f"You are eligible for a Discount of {discount}%")
                print(f"Your discounted Price for the Book is {discounted_price:.2f} MRP")
                cont=input("Do you want to continue? (yes/no): ").strip().lower()
                if cont!='yes':
                    break
            except ValueError as e:
                print(f"Invalid input: {e}")
# Run the bookstore system
if __name__ == "__main__":
    store = BookStore()
    store.process_customer()
