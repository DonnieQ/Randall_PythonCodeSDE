#!/usr/bin/env python3
#adds
def add(x, y):
    return x + y

#subtracts
def subtract(x, y):
    return x - y

#divides
def divide(x, y):
    return x / y

#multiplies
def multiply(x, y):
    return x * y

print("************ Welcome To My Calculator!!**************")
print("*****************************************************")
print("******************By. Randizzle**********************")

calc = True


while calc:
    try:
        data = (input("Press 1, 2, 3, or 4 to select operator!\n1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Quit\n: "))
    except:
        print("Only numbers please")
    # Check if data is one of the five options
    if data in ('1', '2', '3', '4', '5'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if data == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif data == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif data == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif data == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif data == '5':
            calc = False
            break
    else:
        print("Invalid Input")
