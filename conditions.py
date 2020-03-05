# boolean variables evaluate conditions
# true or false is returned when an expression is compared or evaluated
# will evaluate exactly as written / literal interpretations
x = 5
print(x == 5)
print(x == 10)
print(x < 2)
print(x > 2)
print(x < 8)
print(x > 8)
# double equals ( == ) used in comparison between two variables
# not equals operator ( != )

# "and" & "or" boolean operators can be used in expressions
# if / and conditions
name = "trini"
state = "texas"
if name == "trini" and state == "texas":
    print("My name is trini, and I am from Texas")

if state == "florida" or state == "hawaii":  # condition is false as state is defined as "texas"
    print("I would like to go to florida or hawaii") # will not print string due to false

age = int(input("type your age: ")) # interactive example
if age >= 21:
    print("I am of age.")
elif 18 <= age < 21:
    print("I'm almost there.") # based on the first expression is false - "else if"
else:
    print("I am too young.") # else - does not require conditional statement

movie = "love actually"
activity = "tennis"
if movie == "love actually" or activity == "swimming": # if one is true, the condition will return true
    print("I like romantic comedies.")

# in operator - checks if a specified object exists in an iterable object ie. lists
color = "pink"
if color in ["red", "orange", "pink"]:
    print("this is the best color!")

favorite_show = "friends"
tv_shows = ["the office", "you", "friends", "greys anatomy"]
if favorite_show in tv_shows:
    print("this is the best show ever!")

# "not" operator - inverts an expression
sibling = "brian"
if sibling is not "tracy":
    print("I am not related to them.")
