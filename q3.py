def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    if not isinstance(dct, dict):
        return -1
    
    # Check if the key exists in the dictionary
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    else:
        print(f"Adding new key '{key}' with value '{value}'")

    # Update the dictionary with the new key-value pair
    dct[key] = value
    print(f"Updated dictionary: {dct}")
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

print(update_dictionary({}, "name", "Alice"))  
"""
# Should return 
    Adding new key 'name' with value 'Alice'
    Updated dictionary: {'name': 'Alice'}
    {'name': 'Alice'}
"""
print(update_dictionary({"age": 25}, "age", 26))  # Should print "Original value for 'age': 25" and return {'age': 26}
"""
# Should return
    Original value for 'age': 25
    Updated dictionary: {'age': 26}
    {'age': 26}
"""
