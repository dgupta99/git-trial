# main.py

def greet_user():
    print("Hello! Welcome to the simple Python program.")

def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    greet_user()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {sum_two_numbers(num1, num2)}.")
