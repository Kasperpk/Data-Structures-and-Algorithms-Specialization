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
