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


# "break" and "continue" statements:
    # "break" - use to exit "for" or "while" loops
    # "continue" - use to skip current block, and return to "for" or "while" statements
z = 20
while z > 10:
    z = z + 2
    print(z)
    if z >= 30:
        break # stops the loop when z equals to or greater than 30

for b in range(20):
    if b % 2 == 0:    # will check for even numbers
        continue      # continue = passes all the b values that makes the expression above true
    print(b)   # will only print odd numbers

h = 25
while h < 30:
    h = h + 1   # will keep adding 1 until reaches 30
    print(h)
else:       # once 30 is reach = will not print(h) and follow through else statement
    print("value not in range.")

for c in range(10):
    if c % 2 == 0:  # nothing will return from this because 0 will break the loop on the first go
        break
    print(c)
else:
    print("unable to print invalid c value.")
