first_name=input("Enter First Name: ")
last_name=input("Enter Last Name: ")
college_name=input("Enter College Name: ")
department=input("Enter Department: ")
mobile_number=input("Enter Mobile Number: ")
# Outputs
full_name=f"{first_name} {last_name}"
print(f"Your Name is: {full_name}")
print(f"Your College Name: {college_name} Department of {department}")
# ASCII values of Name
ascii_name=", ".join([f"{char}-{ord(char)}" for char in full_name if char.isalnum()])
print(f"ASCII value of Name: {ascii_name}")
# ASCII values of Mobile Number
ascii_mobile=", ".join([f"{num}-{ord(num)}" for num in mobile_number])
print(f"ASCII value of Mobile Number: {ascii_mobile}")
# ASCII Addition Result (with condition to handle mismatched lengths)
print("Result of Addition:")
for i in range(min(len(full_name.replace(" ", "")), len(mobile_number))):
    name_char=full_name.replace(" ", "")[i]
    mob_char=mobile_number[i]
    addition_result=ord(name_char)+ord(mob_char)
    print(f"{name_char}+{mob_char}={addition_result}")
"""
val1=int(input("Enter First Value: "))
val2=int(input("Enter Second Value: "))
val3=int(input("Enter Third Value: "))
# Arithmetic Operations
print(f"Addition: {val1 + val2}")
print(f"Subtraction: {val1 - val2}")
print(f"Multiplication: {val1 * val2}")
print(f"Division: {val1 / val2:.2f}")
print(f"Modulus: {val1 % val2}")
# Before Swapping
print("\nBefore Swapping:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")
print(f"Third Value: {val3}")
# Bitwise Swapping
val1=val1^val2^val3
val2=val1^val2^val3
val3=val1^val2^val3
val1=val1^val2^val3
# After Swapping
print("\nAfter Swapping:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")
print(f"Third Value: {val3}")


username = input("Enter Username: ")
# Print Username with Special Characters
print(f'Hi! Your Entered Input is "{username}"')
# Split Characters and Special Characters
letters = "".join([char for char in username if char.isalpha()])
special_chars = "".join([char for char in username if not char.isalnum()])
print(f"Your Entered Characters are: {letters}")
print(f"Your Entered Special Characters are: {special_chars}")
"""
