# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    """read two integers from the user and return them."""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x= int(input("give me x: "))
    y= int(input("give me y: "))
    
    return x, y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # ADD a Docstring for this function
    """Calculate and return the product of a and b divided by their sum."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    mult_result = a * b
    print("mult result:", mult_result)
    add_result = a + b
    print("add result:", add_result)
    final_value = mult_result / add_result
    return final_value

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    """Print the two input numbers and their multadd result in a formatted display."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print("*" * 16)
    print("RESULTS: ")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("=" * 16)
    
    

def main ():
    # ADD a Docstring for this function
    """Run the program by reading two integers, computing their multadd result, and displaying the results."""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    x,y = read_two_ints()
    xy_multadd = compute_multadd(x, y)
    print_fancy(x, y, xy_multadd)
    # TODO: add your call instead of this line

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    # TODO: add your call instead of this line

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    # TODO: add your call instead of this line


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
