def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    if not isinstance(s, str):
        return -1
    
    # Reverse the string using slicing
    reversed_string = s[::-1]
    #print(f"Reversed string: {reversed_string}")
    return reversed_string

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))  
"""
# Should return 
# "dlroW olleH"
"""
print(string_reverse("Python"))    
"""    
# Should return 
# "nohtyP"
"""
