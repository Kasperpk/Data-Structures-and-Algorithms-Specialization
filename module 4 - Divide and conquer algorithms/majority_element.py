def majority_element_rec(arr, left, right):
    """
    Divide and conquer algorithm to find majority element.
    Returns the majority element if it exists, None otherwise.
    """
    # Base case
    if left == right:
        return arr[left]
    
    # Divide
    mid = (left + right) // 2
    left_majority = majority_element_rec(arr, left, mid)
    right_majority = majority_element_rec(arr, mid + 1, right)
    
    # If both halves have the same majority element
    if left_majority == right_majority:
        return left_majority
    
    # Count occurrences of both candidates in the current range
    left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_majority)
    right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_majority)
    
    # Check if either candidate is majority in current range
    range_size = right - left + 1
    if left_count > range_size // 2:
        return left_majority
    elif right_count > range_size // 2:
        return right_majority
    else:
        return None

def has_majority_element(arr):
    """
    Determines if array has a majority element (appears > n/2 times).
    Returns 1 if majority element exists, 0 otherwise.
    """
    if not arr:
        return 0
    
    candidate = majority_element_rec(arr, 0, len(arr) - 1)
    if candidate is None:
        return 0
    
    # Verify the candidate is actually a majority element
    count = sum(1 for x in arr if x == candidate)
    return 1 if count > len(arr) // 2 else 0

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = has_majority_element(arr)
    print(result)