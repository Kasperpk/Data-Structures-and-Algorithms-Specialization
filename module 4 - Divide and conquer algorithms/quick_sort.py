import random

def partition3(arr, left, right):
    """
    3-way partitioning for quicksort.
    Returns (m1, m2) where:
    - arr[left...m1-1] < pivot
    - arr[m1...m2] = pivot  
    - arr[m2+1...right] > pivot
    """
    pivot = arr[left]
    m1 = left  # boundary for elements < pivot
    m2 = right  # boundary for elements > pivot
    i = left
    
    while i <= m2:
        if arr[i] < pivot:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
            # Don't increment i here as we need to check the swapped element
        else:
            i += 1
    
    return m1, m2

def randomized_quick_sort(arr, left, right):
    """
    Randomized quicksort with 3-way partitioning.
    Sorts the array in-place.
    """
    if left >= right:
        return
    
    # Choose random pivot and swap with first element
    k = random.randint(left, right)
    arr[left], arr[k] = arr[k], arr[left]
    
    # 3-way partition
    m1, m2 = partition3(arr, left, right)
    
    # Recursively sort the parts
    randomized_quick_sort(arr, left, m1 - 1)
    randomized_quick_sort(arr, m2 + 1, right)

def quick_sort(arr):
    """
    Main function to sort an array using randomized quicksort.
    """
    if len(arr) <= 1:
        return arr
    
    # Make a copy to avoid modifying original
    result = arr[:]
    randomized_quick_sort(result, 0, len(result) - 1)
    return result

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Sort in-place
    randomized_quick_sort(arr, 0, len(arr) - 1)
    
    # Output the sorted array
    print(' '.join(map(str, arr)))