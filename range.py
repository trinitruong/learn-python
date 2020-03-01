# range() is a function to call upon a number list
def main():
    # create a range generator
    print(range(10))

# for conditional statement= i is variable to find in the range
# range(10) = 0-9 ; will only call one value at a time
    for i in range(10):
        print(i)

    # create a list of ALL the values from the range generator
    # (instead of one at a time on access)
    print(list(range(10)))

    for i in list(range(10)):
        print(i)


if __name__ == "__main__":
    main()
