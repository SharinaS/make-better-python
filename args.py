# ARGS:
# - For non-keyword arguments
# - Used to pass a variable number of arguments
# - When using the "unpacking operator," which is the "*", the iterable object
# you get back is a tuple... which is immutable.
# - The "*" makes the variable associated with it an iterable... as in now you must iterate over it.
# this works well with map, filter, etc. Note that the variable can be whatever you want, though
# traditionally it's "args."
# Define the variables when calling the function - this lets you pass in any number of variables.

def show_cats(*cats) -> None:
    for cat in cats:
        print(cat)


def sum_w_args(*args):
    result = 0
    for int in args:
        result += int
    return result


show_cats('Razzle', 'Fluffy', 'Mikey')
print(sum_w_args(10, 20, 30))


# --- Output from ^ ---
# Razzle
# Fluffy
# Mikey
# 60
