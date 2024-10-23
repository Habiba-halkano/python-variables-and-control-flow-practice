#python project that takes user's ages and categorizes them as :
#minor (under 18), adult (18 -65) or a senior (over 65)

#function definition
def users_ages(age):
    if age < 18:
        print("minor")
    elif age <= 65:
        print("adult")
    else:
        print("senior")

#take user input
age= int(input("Enter your age: "))

#function call
users_ages(age)