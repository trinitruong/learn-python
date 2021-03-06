# simple math: addition, subtraction, multiplication, division operators can be used with numbers
print(2 + 2)
print(36 - 4)
print(4 * 5)
print(12 / 3)
# can use operators with numbers in the function
# can also assign math operators to variable
num1 = 1 + 1
print(num1)
num2 = 2 * 3
print(num2)
num3 = 4 / 2
print(num3)
num4 = 13 - 5
print(num4)

# can use them in combination; follows PEMDAS math rule
combo1 = 20 - 6 * 3
print(combo1)

combo2 = 3 + 4 - 1 * 20 / 2
print(combo2)

# can use the math operators if variables have numbers as values
combo3 = num4 - num1
print(combo3)

print(num4 - num3 + num1)

print(num1 * num4)

# modulo (%) operator = returns the integer of the remainder of a division
# dividend % divisor
remainder = 23 % 6 # equals to 3r5 = print 5
print(remainder)

print(14 % 3) # equals 4r2 = print 2

# two multiplication symbols ** = power relationship a^b = a ** b
squared = 4 ** 2
print(squared)

cubed = 3 ** 3
print(cubed)

print(2 ** 4) #equals 2^4

# double forwardslash ( // ) will divide an expression & return without a decimal
print (23 // 4)

# addition can be used with strings
petname = "sweet" + "heart"
print(petname)

# multiplying strings = form a string with repeating sequence
multiple_yays = "yay" * 8
print(multiple_yays)

# multiply lists = repeat lists sequence multiple times
print([3,4,5] * 3)
print(["blue", "green", "purple"] * 4)

color = ["red", "orange", "yellow", "blue"]
print(color * 2)

# lists can be joined together using addition operator
favorite_numbers = [2,3,5,16,21]
lucky_numbers = [1,4,7]
fav_lucky_numbers = favorite_numbers + lucky_numbers
print(fav_lucky_numbers)

family_names = ["tracy", "brian", "brandon"]
friend_names = ["tammy", "rachel", "kenny", "joy"]
family_n_friend_names = family_names + friend_names
print(family_n_friend_names)


# Comparison Operators: compare the values on either side & determine relationship
# use any of the operators below to determine relationships of values:
# a == b: values are equal
# a != b: a does NOT equal b
# a <> b: a does NOT equal b
# a > b ; a < b
# a >= b: a is greater than or equal to b
# a <= b: a is less than or equal to b


# Assignment operator: holds a variable & adds on other operators
# assignment operators do NOT return anything, must print after use
# start with assigning a variable
c = 5

# to add on to the variable use : +=
# c += 2 is equivalent to c = c + 2
c +=2
print(c)

# to subtract from variable use: -=
# c -= 2 is equivalent to c = c - 2
c -=2
print(c)

# to multiply variable use: *=
# c *= 2 is equivalent to c = c * 2
c *=2
print (c)

# to divide variable use: /=
# c /= 2 is equivalent to c = c / 2
c /= 2
print(c)

# to find remainder of a division from variable use: %=
# c %= 2 is equivalent to c = c % 2
c %= 2
print(c)

#to perform exponential (power) calculation on variable use: **=
# c ** 2 is equivalent to c = c ** 2
c ** 2
print(c)

# the assignment operator builds upon each other when using the same letter multiple times in a row
