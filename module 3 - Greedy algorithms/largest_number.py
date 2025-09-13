from functools import cmp_to_key

def largest_number(numbers):
    """
    Arrange the given numbers to form the largest possible number.
    
    Uses greedy algorithm with custom comparator: for numbers a and b,
    compare ab vs ba and choose the arrangement that gives larger result.
    """
    if not numbers or all(num == '0' for num in numbers):
        return '0'
    
    # Convert all numbers to strings for concatenation
    str_numbers = [str(num) for num in numbers]
    
    # Custom comparator: compare ab vs ba
    def compare(x, y):
        if x + y > y + x:
            return -1  # x should come before y
        elif x + y < y + x:
            return 1   # y should come before x
        else:
            return 0   # order doesn't matter
    
    # Sort using the custom comparator
    str_numbers.sort(key=cmp_to_key(compare))
    
    # Concatenate the sorted numbers
    result = ''.join(str_numbers)
    
    # Handle edge case where result might be all zeros
    if result[0] == '0':
        return '0'
    
    return result

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    numbers = input().split()
    
    result = largest_number(numbers)
    print(result)