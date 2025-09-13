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
