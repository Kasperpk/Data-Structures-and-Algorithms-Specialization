import random
import sys

def quicksort(arr, left=0, right=None):
    """
    3-way quicksort implementation that handles duplicates efficiently.
    
    Args:
        arr: Array to sort
        left: Left boundary
        right: Right boundary
        
    Time complexity: O(n log n) average, O(n^2) worst case
    Space complexity: O(log n) average due to recursion
    """
    if right is None:
        right = len(arr) - 1
    
    if left >= right:
        return
    
    # Use 3-way partitioning for better performance with duplicates
    lt, gt = partition3(arr, left, right)
    
    quicksort(arr, left, lt - 1)
    quicksort(arr, gt + 1, right)


def partition3(arr, left, right):
    """
    3-way partition: elements < pivot | elements = pivot | elements > pivot
    
    Returns:
        (lt, gt) where:
        - elements [left...lt-1] < pivot
        - elements [lt...gt] = pivot  
        - elements [gt+1...right] > pivot
    """
    # Choose random pivot to avoid worst-case on already sorted arrays
    pivot_idx = random.randint(left, right)
    arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
    
    pivot = arr[left]
    lt = left      # arr[left+1...lt-1] < pivot
    i = left + 1   # arr[lt...i-1] = pivot
    gt = right     # arr[gt+1...right] > pivot
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt


def randomized_quicksort(arr):
    """
    Main function for randomized quicksort.
    Sorts the array in-place.
    
    Args:
        arr: Array of integers to sort
        
    Returns:
        None (sorts in-place)
    """
    if len(arr) <= 1:
        return
    
    # Set recursion limit to handle large inputs
    sys.setrecursionlimit(10000)
    quicksort(arr)


# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input().split()))
    
    randomized_quicksort(arr)
    print(' '.join(map(str, arr)))