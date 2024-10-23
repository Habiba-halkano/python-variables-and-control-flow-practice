#python program that asks a user to enter a number 1-7 and prints corresponding day of the week. For number outside range print "invalid input"

#function definition
def days_of_week(num):
    if (num == 1):
        print("Monday")
    elif (num == 2):
        print("Tuesday")
    elif (num == 3):
        print("Wednesday")
    elif (num == 4):
        print("Thursday")
    elif (num == 5):
        print("Friday")
    elif (num == 6):
        print("Saturday")
    elif (num == 7):
        print("Sunday")
    else:
        print("Invalid input")

#prompt user
num = int(input("Enter a number: "))

#function call
days_of_week(num)
