class CreditCardPayment:
    def pay(self,amount):
        return f"paid {amount} using creditcard"
class PayPalPayment:
    def pay(self,amount):
        return f"paid {amount} using PayPal"
class DebitCardPayment:
    def pay(self,amount):
        return f"paid {amount} using debitcard"
class payment:
    def show(self,amount):
        return f"paid {amount}"
def process_payment(ccp,amount):
    print(ccp.pay(amount))
cc=CreditCardPayment()
process_payment(cc,200)
pp=PayPalPayment()
process_payment(pp,200)
dp=DebitCardPayment()
process_payment(dp,400)

