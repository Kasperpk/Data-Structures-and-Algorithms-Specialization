def merge_and_count(arr, temp, left, mid, right):
    """
    Merge two sorted subarrays and count inversions.
    Returns the number of inversions between the two subarrays.
    """
    i, j, k = left, mid + 1, left
    inv_count = 0
    
    # Merge the two subarrays while counting inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            # arr[i] > arr[j], so there are (mid - i + 1) inversions
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    # Copy remaining elements
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # Copy back the merged elements to original array
    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    """
    Divide and conquer algorithm to count inversions using merge sort.
    Returns the number of inversions in the array.
    """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        
        # Count inversions in left half
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        
        # Count inversions in right half
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        
        # Count inversions between the two halves
        inv_count += merge_and_count(arr, temp, left, mid, right)
    
    return inv_count

def count_inversions(arr):
    """
    Count the number of inversions in an array.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
    Time complexity: O(n log n)
    """
    if len(arr) <= 1:
        return 0
    
    # Create a temporary array for merging
    temp = [0] * len(arr)
    
    # Make a copy to avoid modifying the original array
    arr_copy = arr[:]
    
    return merge_sort_and_count(arr_copy, temp, 0, len(arr) - 1)

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = count_inversions(arr)
    print(result)