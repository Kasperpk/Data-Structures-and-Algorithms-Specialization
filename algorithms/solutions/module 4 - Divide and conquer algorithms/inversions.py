def merge_and_count(arr, temp_arr, left, mid, right):
    """
    Merge two sorted halves and count inversions.
    
    Args:
        arr: Original array
        temp_arr: Temporary array for merging
        left: Left boundary
        mid: Middle point
        right: Right boundary
        
    Returns:
        Number of inversions found during merge
    """
    i, j, k = left, mid + 1, left
    inv_count = 0
    
    # Merge the two halves while counting inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # arr[i] > arr[j], so there are (mid - i + 1) inversions
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    # Copy remaining elements
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    # Copy back the merged elements to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    """
    Merge sort that counts inversions using divide and conquer.
    
    Args:
        arr: Array to sort
        temp_arr: Temporary array
        left: Left boundary
        right: Right boundary
        
    Returns:
        Number of inversions in the array
    """
    inv_count = 0
    
    if left < right:
        mid = left + (right - left) // 2
        
        # Recursively count inversions in left and right halves
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        
        # Count inversions between left and right halves
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    
    return inv_count


def count_inversions(arr):
    """
    Count number of inversions in array using divide and conquer.
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    
    Args:
        arr: Array of integers
        
    Returns:
        Number of inversions
        
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(arr) <= 1:
        return 0
    
    # Create a copy to avoid modifying original array
    temp_arr = [0] * len(arr)
    arr_copy = arr[:]
    
    return merge_sort_and_count(arr_copy, temp_arr, 0, len(arr_copy) - 1)


# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input().split()))
    
    result = count_inversions(arr)
    print(result)