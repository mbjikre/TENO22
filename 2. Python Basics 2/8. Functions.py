def adl():
    res = v1 + v2
    print(res)

v1 = int(input())
v2 = int(input())
adl()
#print(f'{adl()}')

def adl(v1=int(input()),v2=int(input())):
    #res = v1 + v2
    print(f'Output: {v1+v2}')

adl()
#print(f'{adl()}')


#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

def cheDriverAge(age=int(input("What is your age?: "))):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.
#age = int(input("What is your age?: "))
cheDriverAge()

def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge(18)