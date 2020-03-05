# two types: for and while
months = ["may", "june", "july", "august"]
month = input("What month is it?\n")
if month in months:
    print("Summer time!")

# "for" loop = executes a sequence multiple times and abbreviates the code that controls the loop variable
color = input('what color is in the rainbow?\n')
rainbow = ["red","orange","yellow","green","blue","indigo","violet"]

for color in rainbow:
    print("taste the rainbow!")

x = 15 # while loop will continue to subtract until the while statement is false
while x > 10:
    x = x - 1
    print(x)


# "while" loop = repeats statement while a given condition is TRUE ; tests condition before executing
