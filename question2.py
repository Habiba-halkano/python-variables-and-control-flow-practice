#python program that asks a user for a number and prints whether the number is odd or even
#define function to check
def even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

#prompt user to enter a number
num = int(input("Enter a number: "))

#call the function
even_or_odd(num)

