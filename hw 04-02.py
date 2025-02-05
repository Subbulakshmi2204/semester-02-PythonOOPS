def length_of_last_word():
    s=input("Enter a string: ")
    print("Length of last word:", len(s.strip().split()[-1]))
length_of_last_word()


def add_binary():
    a=input("Enter first binary string: ")
    b=input("Enter second binary string: ")
    print("Sum of binary strings:", bin(int(a,2)+int(b,2))[2:])
add_binary()
