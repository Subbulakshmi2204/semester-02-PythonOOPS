from abc import ABC, abstractmethod
class AbstractBase(ABC):
    @abstractmethod
    def welcome(self):
        pass
    @abstractmethod
    def test_data(self, name):
        pass
    @abstractmethod
    def count_vowels(self, name):
        pass
    @abstractmethod
    def calculate_grade(self, mark1, mark2):
        pass
# Concrete Class Implementation
class Operations(AbstractBase):
    def welcome(self):
        print("Welcome To WTS!\nWe wish you the Best!!")
    def test_data(self, name):
        print(f"Welcome {name}!\nHave a nice day!")
    def count_vowels(self, name):
        vowels = 'aeiou'
        vowel_count = {v: 0 for v in vowels}
        total_count = 0
        for char in name.lower():
            if char in vowels:
                vowel_count[char] += 1
                total_count += 1
        print(f"Count of Vowels are: {total_count}")
        for vowel, count in vowel_count.items():
            if count > 0:
                print(f"{vowel}: {count}")
    def calculate_grade(self, mark1, mark2):
        total_marks = mark1 + mark2
        if total_marks > 95:
            grade = 'E'
        elif 80 <= total_marks <= 95:
            grade = 'A+'
        elif 75 <= total_marks < 80:
            grade = 'A'
        elif 60 <= total_marks < 75:
            grade = 'B'
        else:
            grade = 'F'
        print(f"Total Marks: {total_marks}\nGrade: {grade}")


# Looping and Conditional Statements
class PasswordFilter:
    def __init__(self, password):
        self.password = password
    def validate_password(self):
        result = ''.join([char for char in self.password if not char.isdigit()])
        print(f"Filtered Password (without numerical values): {result}")
# Main Function to Demonstrate
if __name__ == "__main__":
    # Abstract Class Demonstration
    obj = Operations()
    obj.welcome()
    # Test Data Method
    name = input("Please input a name: ")
    obj.test_data(name)
    # Count Vowels Method
    obj.count_vowels(name)
    # Calculate Grade Method
    mark1 = int(input("Enter Mark1: "))
    mark2 = int(input("Enter Mark2: "))
    obj.calculate_grade(mark1, mark2)
    # Password Filter Demonstration
    password = input("Enter a password: ")
    password_filter = PasswordFilter(password)
    password_filter.validate_password()
