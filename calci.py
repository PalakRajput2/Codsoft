print("This is a basic calculator made in Python ")
print("************")
print()
import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def sqt(x):
    return math.sqrt(x)
  

print("Select operation that you want to perform ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square root")
while True:
    choice = input("Enter the number of your choice ")

    if choice in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Sum of ",num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("Subtraction of",num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("Multiplication of ",num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("Division of ",num1, "/", num2, "=", divide(num1, num2))
        
        elif choice =='5':
            print("Square root of", num1,"is:", sqt(num1))
            print("Square root of", num2,"is:", sqt(num2))
       
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("The Input is Invalid!!! Try again  ")