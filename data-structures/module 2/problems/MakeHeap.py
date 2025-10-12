def build_heap(data):
    """
    Build a min-heap from an array and return the sequence of swaps.
    """
    swaps = []
    size = len(data)
    
    def sift_down(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < size and data[left] < data[min_index]:
            min_index = left
            
        if right < size and data[right] < data[min_index]:
            min_index = right
            
        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            sift_down(min_index)
    
    # Build heap by sifting down each non-leaf node
    for i in range(size // 2, -1, -1):
        sift_down(i)
        
    return swaps

def main():
    # Read input
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    
    # Generate swaps to build min heap
    swaps = build_heap(data)
    
    # Output results
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()