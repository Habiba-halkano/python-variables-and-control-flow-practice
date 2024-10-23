#python program that takes a score as input and categories it into the following grades:
#A (90 - 100)
#B (80 - 89)
#C (70 - 79)
#D (60 - 69)
#F (BELOW 60)

#Defining function
def grading_score(score):
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')

#prompt user to enter score
score = int(input('Enter your score: '))

#function call
grading_score(score)