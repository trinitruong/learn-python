# can contain any variable
# use bracket operators []
# the values are in a sequence defined by its position or index *starting at 0*
numbers = [1,2,3,7,8,9]
print(numbers)
print(numbers[4])

# this will cause an error: print(numbers[0,2,3])

strings = ["example", "practice", "sample"]
print(strings)
print(strings[0]) # when indexing lists, always start at 0

names = ["omar", "tracy", "tammy", "katie", "brian"]
print(names)
print(names[0])

education = ['physics', 'calculus', 2012, 2017]
print(education)

# to print multiple variables from list, call on each index individually & use comma inbetween
print(education[3], education[1])

# tuples = sequences like lists:
    # unlike lists, tuples use paranthesis () & cannot be changed
