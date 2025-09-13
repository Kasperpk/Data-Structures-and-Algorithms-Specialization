def merge(arr, temp_arr, left, mid, right):
    """
    Merge two sorted halves of an array.
    
    Args:
        arr: Original array
        temp_arr: Temporary array for merging
        left: Left boundary
        mid: Middle point  
        right: Right boundary
    """
    i, j, k = left, mid + 1, left
    
    # Merge the two halves
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
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
    
    # Copy back to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]


def merge_sort_recursive(arr, temp_arr, left, right):
    """
    Recursive merge sort implementation.
    
    Args:
        arr: Array to sort
        temp_arr: Temporary array
        left: Left boundary
        right: Right boundary
    """
    if left < right:
        mid = left + (right - left) // 2
        
        # Sort left and right halves
        merge_sort_recursive(arr, temp_arr, left, mid)
        merge_sort_recursive(arr, temp_arr, mid + 1, right)
        
        # Merge the sorted halves
        merge(arr, temp_arr, left, mid, right)


def merge_sort(arr):
    """
    Merge sort algorithm using divide and conquer.
    Sorts the array in-place.
    
    Args:
        arr: Array of integers to sort
        
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(arr) <= 1:
        return
    
    temp_arr = [0] * len(arr)
    merge_sort_recursive(arr, temp_arr, 0, len(arr) - 1)


# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input().split()))
    
    merge_sort(arr)
    print(' '.join(map(str, arr)))