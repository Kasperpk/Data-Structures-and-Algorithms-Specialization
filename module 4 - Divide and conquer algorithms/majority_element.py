def majority_element(arr):
    """
    Find majority element using divide and conquer approach.
    A majority element appears more than n/2 times in an array of size n.
    
    Args:
        arr: Array of integers
        
    Returns:
        1 if majority element exists, 0 otherwise
        
    Time complexity: O(n log n)
    Space complexity: O(log n) due to recursion
    """
    def find_majority_element(arr, left, right):
        """Helper function that returns the majority element or None"""
        # Base case
        if left == right:
            return arr[left]
        
        # Divide
        mid = left + (right - left) // 2
        left_majority = find_majority_element(arr, left, mid)
        right_majority = find_majority_element(arr, mid + 1, right)
        
        # If both halves have the same majority element
        if left_majority == right_majority:
            return left_majority
        
        # Count occurrences of both candidates in the current range
        left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_majority)
        right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_majority)
        
        # Return the element that appears more than half the time
        if left_count > (right - left + 1) // 2:
            return left_majority
        elif right_count > (right - left + 1) // 2:
            return right_majority
        else:
            return None
    
    if not arr:
        return 0
    
    # Find the majority element candidate
    candidate = find_majority_element(arr, 0, len(arr) - 1)
    
    if candidate is None:
        return 0
    
    # Verify that the candidate is actually a majority element
    count = sum(1 for x in arr if x == candidate)
    return 1 if count > len(arr) // 2 else 0


def majority_element_optimized(arr):
    """
    Optimized approach using Boyer-Moore Voting Algorithm.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not arr:
        return 0
    
    # Phase 1: Find candidate
    candidate = arr[0]
    count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = arr[i]
                count = 1
    
    # Phase 2: Verify candidate
    count = sum(1 for x in arr if x == candidate)
    return 1 if count > len(arr) // 2 else 0


# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input().split()))
    
    result = majority_element_optimized(arr)
    print(result)