#python program that takes two numbers and an operation from the user, performs the operation and prints the result
#function definition
def number_operation(num1, num2, operation):
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
    elif operation == '%':
        print(num1 % num2)
    elif operation == '//':
        print(num1 // num2)

#prompt user to enter numbers and operation
num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
operation = input("Enter operation: ")

#function call
number_operation(num1, num2, operation)