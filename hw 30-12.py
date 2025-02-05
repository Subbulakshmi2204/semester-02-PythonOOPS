
class Count_:
    def __init__(self,string):
        self.string=string
    def count_alphabet(self):
        alpha_count=0
        num_count=0
        spl_count=0
        for char in string:
            if char.isalpha():
                alpha_count+=1
            elif char.isdigit():
                num_count+=1
            else:
                spl_count+=1
        return alpha_count,num_count,spl_count
string=input("Enter a string:")
analyse=Count_(string)
alphabet,numeric,special=analyse.count_alphabet()
print(f"Alphabetic Characters:{alphabet}")
print(f"Numeric Characters:{numeric}")
print(f"Special Characters:{special}")

class Stringanalyzer:
    def __init__(self,input_string):
        self.input_string=input_string
    def count_chars(self):
        alpha_count=0
        num_count=0
        spl_count=0
        for char in input_string:
            if char.isalpha():
                alpha_count+=1
            elif char.isdigit():
                num_count+=1
            else:
                spl_count+=1
        return alpha_count,num_count,spl_count
    def validate_string(self):
        has_alphabet=any(char.isalpha() for char in self.input_string)
        has_special=any(not char.isalnum() for char in self.input_string)
        return has_alphabet and has_special
input_string=input("Enter a string: ")
analyzer=Stringanalyzer(input_string)
if analyzer.validate_string():
    print("The string contains both alphabets and special characters.")
else:
    print("The string does not contain both alphabets and special characters.")
