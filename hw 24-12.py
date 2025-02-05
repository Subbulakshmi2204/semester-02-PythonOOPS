class E_commerce:
    def calculate_final_price(self,pro_price,disct,tax):
        if pro_price<=0 or disct<=0 or tax<=0:
            raise ValueError("Base price, Discount, Tax cannot be in negative")
        disct_price=pro_price*(disct/100)
        tax_price=pro_price*(tax/100)
        tot_price=disct_price+tax_price
        print(f"The total amount of the product is:{tot_price:.2f}")
ecom=E_commerce()
try:
    price=int(input("Enter the price of the product:"))
    discount=int(input("Enter the discount:"))
    tax=int(input("Enter the tax:"))
    ecom.calculate_final_price(price,discount,tax)
except ValueError as e:
    print(e)
