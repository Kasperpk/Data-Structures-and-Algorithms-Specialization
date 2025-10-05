def min_heapify(n,integers):
    '''
    Function to create heap from array of integers 
    '''
    def heapify(integers, i, n):
        smallest = i
        # finding childs of the parent
        left = 2*i+1
        right = 2*i+2

        if left < n and integers[left] < integers[smallest]:
            # check if left child is less than current value at parent index
            smallest = left 
            
        if right < n and integers[right] < integers[smallest]:
            # check if right child is less than current value at parent index
            smallest = right
            
        # if the smallest value is not the parent index, then swap with the smallest value
        if smallest != i:
            temp = integers[i]
            integers[i] = integers[smallest]
            integers[smallest] = temp
            heapify(integers, smallest, n)

    for i in range(n//2 - 1,-1,-1): 
        heapify(integers, i, n)

    return integers

if __name__ == '__main__':
    n = int(input())
    integers = []
    for i in range(0,n):
        integer = int(input())
        integers.append(integer)
    result=(min_heapify(n, integers))
    print(result)