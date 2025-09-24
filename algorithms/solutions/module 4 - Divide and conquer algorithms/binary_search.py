def binary_search_with_duplicates(arr, target):
    """
    Binary search that finds the first occurrence of target in array with duplicates.
    
    Args:
        arr: Sorted array of integers (may contain duplicates)
        target: Integer to search for
    
    Returns:
        Index of first occurrence of target if found, -1 otherwise
        
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            # Continue searching in left half for first occurrence
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result


# Input/Output handling for Coursera format
if __name__ == "__main__":
    # Read input: first line has array size, second line has array elements,
    # third line has number of queries, fourth line has query elements
    n = int(input())
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input().split()))
    
    k = int(input())
    if k == 0:
        queries = []
    else:
        queries = list(map(int, input().split()))
    
    # Process each query
    results = []
    for target in queries:
        result = binary_search(arr, target)
        results.append(str(result))
    
    print(' '.join(results))
