def binary_search(arr, x):
    """
    Binary search algorithm for finding an element in a sorted array.
    Returns the index of the element if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_with_duplicates(arr, x):
    """
    Binary search algorithm that finds the first occurrence of an element
    in a sorted array that may contain duplicates.
    Returns the index of the first occurrence if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            # Continue searching in the left half to find first occurrence
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Input/Output handling for Coursera format
if __name__ == "__main__":
    # Read the array
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Read the number of queries
    k = int(input())
    queries = list(map(int, input().split()))
    
    # Process each query
    results = []
    for x in queries:
        result = binary_search(arr, x)
        results.append(result)
    
    # Output results
    print(' '.join(map(str, results)))