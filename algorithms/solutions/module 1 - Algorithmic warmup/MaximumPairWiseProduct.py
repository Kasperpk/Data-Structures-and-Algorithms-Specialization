def max_pairwise_product_fast(numbers):
    n = len(numbers)
    if n < 2:
        return 0
    
    # Find indices of two largest numbers
    first_max_idx = 0
    for i in range(1, n):
        if numbers[i] > numbers[first_max_idx]:
            first_max_idx = i
    
    # Find second largest (different index)
    second_max_idx = 1 if first_max_idx == 0 else 0
    for i in range(n):
        if i != first_max_idx and numbers[i] > numbers[second_max_idx]:
            second_max_idx = i
    
    return numbers[first_max_idx] * numbers[second_max_idx]

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    result = max_pairwise_product_fast(numbers)
    print(result)
