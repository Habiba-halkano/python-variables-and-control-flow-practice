#pyton program that checks whether password entered by user is "python123" if it is, output is access granted, otherwise access denied

#function definition
def check_password(password):
    if password == 'python123':
        print("Access granted")
    else:
        print("Access denied")

#taking user input
password = input("Enter your password: ")

#function call
check_password(password)
