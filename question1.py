def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap without using a third variable
    x = x + y
    y = x - y
    x = x - y

    print("x: ", x, "  y: ", y)

    """
    Task 2
    # Invoke the function "swap" using the following scenarios:
    # - "Apple", 10
    # - 9, 17
    """
    swap(10, 20)
    # Output: x: 20  y: 10

    swap("a", 5)
    # Output: -1
