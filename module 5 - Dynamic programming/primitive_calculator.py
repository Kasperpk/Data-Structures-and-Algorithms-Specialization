def primitive_calculator(n):
    """
    Find the minimum number of operations to reduce a positive integer n to 1.
    Allowed operations:
    1. Multiply by 2
    2. Multiply by 3  
    3. Add 1
    
    This is solved by reversing the problem: start from 1 and reach n using:
    1. Divide by 2 (if even)
    2. Divide by 3 (if divisible by 3)
    3. Subtract 1
    
    Args:
        n: Target number
        
    Returns:
        Minimum number of operations needed
        
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if n == 1:
        return 0
    
    # dp[i] = minimum operations to reach 1 from i
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case
    
    for i in range(2, n + 1):
        # Operation 3: subtract 1 (always possible)
        dp[i] = dp[i - 1] + 1
        
        # Operation 1: divide by 2 (if i is even)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # Operation 2: divide by 3 (if i is divisible by 3)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]


def primitive_calculator_with_sequence(n):
    """
    Returns both the minimum operations and the sequence of numbers.
    
    Returns:
        Tuple of (min_operations, sequence)
    """
    if n == 1:
        return 0, [1]
    
    dp = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        # Subtract 1
        if dp[i - 1] + 1 < dp[i]:
            dp[i] = dp[i - 1] + 1
            parent[i] = i - 1
        
        # Divide by 2
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            parent[i] = i // 2
        
        # Divide by 3
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            parent[i] = i // 3
    
    # Reconstruct sequence
    sequence = []
    current = n
    while current != -1:
        sequence.append(current)
        current = parent[current]
    
    sequence.reverse()
    return dp[n], sequence


# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    min_ops, sequence = primitive_calculator_with_sequence(n)
    print(min_ops)
    print(' '.join(map(str, sequence)))