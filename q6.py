def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """

    if not isinstance(lst, list):
        return -1
    
    index = 0
    while index < len(lst):
        if isinstance(lst[index], (int, float)) and lst[index] < 0:
            #print(f"First negative number found: {lst[index]}")
            return lst[index]
        index += 1
    #print("No negatives found")

    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print(find_first_negative([3, 5, -1, 7, -2, 8]))  # Should return -1
print(find_first_negative([2, 10, 7, 0]))          # Should return "No negatives"