def calculate_fare(mile,time):
    return mile*1.50+2.50+time*0.25
try:
    mile=int(input("Enter the value in mile:"))
    time=int(input())
    if mile<0 and time<0:
        raise ValueError
finally:
    tot_fare=calculate_fare(mile,time)
    print("The total amount is:",tot_fare)
