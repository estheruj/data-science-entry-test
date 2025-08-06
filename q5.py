def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return -1
    
    if divisor == 0:
        return -1
    
    is_divisible = num % divisor == 0
    #print(f"Is {num} divisible by {divisor}? {is_divisible}")
    return is_divisible



# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))  
"""
# Should return
# True
"""
print(check_divisibility(7, 3))
"""
# Should return
# False
"""
