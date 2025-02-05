class Calculator:
    def calculate(self,a,b=None,c=None):
        if b is None and c is None:
            return a**2
        elif c is None:
            return a+b
        else:
            return a*b*c
cal=Calculator()
print(cal.calculate(2))
print(cal.calculate(5,9))
print(cal.calculate(2,5,9))
