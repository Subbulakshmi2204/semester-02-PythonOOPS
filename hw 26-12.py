class Calculate:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            raise ZeroDivisionError("Division by zero is not allowed..")
        return a/b
def calculate():
    calc=Calculate()
    operation={'+':calc.add,'-':calc.sub,'*':calc.mul,'/':calc.div}
while True:
    try:
        a=float(input("Enter any number:"))
        b=float(input("Enter any number:"))
    except ValueError:
        print("Invalid input please enter numeric values..")
        continue
    try:
        operation=input("Enter any operations(+,-,/,*):")
        if operation not in operation:
            print("Invalid operation!!Please choose from the given operations..")
            continue
        result=operation[operation](a,b)
        print(f"The result is :{result}")
    except ZeroDivisionError as ze:
        print(ze)
    except TypeError as te:
        print(te)
    except KeyError:
        print("Invalid operation..Please try again..")
    except Exception as e:
        print(f"An unexpected error occured:{e}")
calculate()
