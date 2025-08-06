def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1     

    # Swapping values using arithmetic operations
    x = x + y  
    y = x - y
    x = x - y
   
    # Print the swapped values
    print(f"Swapped values: x = {x}, y = {y}")

    return


"""
# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
"""

swap("Apple", 10)  # Should return -1
swap(9, 17)        # Should print Swapped values: x = 17, y = 9
