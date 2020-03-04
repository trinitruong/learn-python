# strings = characters in quotes
# single and double quotes are same in python
# string format operator = % -- will format a set of variables enclosed in a tuple
    #tuple = fixed size list: contains normal text, 'argument specifiers' and special symples like %s and %d
# calls on the arguments in order
# %s - calls on string
# %d - integer
# %f - floating point numbers
# %.<number of digits>f - floating point numnbers with a fixed amount of digits to the right of the dot
# %x/%X - integers in hex representation (lowercase/uppercase)

place = "cancun"
year = 2020
print("We would love to go to %s in %s!" % (place, year))

# basic string operations
string = "hello world"
print(len(string)) # len() will return the length (number of items) of string ; spaces are count as 1

print(string.index("o")) # will return "o" in "hello world" as an integer

print(string.count("l")) #counts how many "l" in the string

# square brackets [] can slice a string
print(string[2:5]) # will print letters/spaces that are indexed 2-5 ; spaces count when indexing
# first number is inclusive and last number is exclusive
print(string[2:-1]) # negative number = start count from the end
print(string[::2]) # [start:stop:step] - last colon will skip over specified step to skip
