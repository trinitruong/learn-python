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
