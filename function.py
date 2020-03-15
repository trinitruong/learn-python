# use functions to divide code into blocks, order code, resuse it and save time
# functions = key way to define interfaces
# block = area of code written in format of : block_head..new line + indention for following block line
# block line = python code
# block keywords : "def", "if", "for", and "while"
# every func def starts with a colon (:)

def example_function():       # line 6 & 7 = func definition
    print("this is a block.")
example_function()            # line 8 = func call

# function may receive arguments - variables passed from caller to the function
def function_with_args(name, greeting):
    print("hello, %s, I wish you %s"%(name, greeting))
function_with_args("omar", "the best!")

# functions may return a value to the caller - use keyword "return" - specifies what value to give back to caller of function
# statement return = expression
# return statement with no args = same as return none
def sum_example(a,b): # line 20 and 21 = function definition ; a,b = declaring arguments
    return a + b
x = sum_example(3,4) # line 22 = function call & output is none b/c dose not return anything, but holds value
# line 22: 3,4 = passing arguments
print(sum_example(3,4)) # using print command = outputs 7
