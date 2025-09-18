def knapsack_01(capacity, weights, values):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    Each item can either be taken completely or not taken at all.
    
    Args:
        capacity: Maximum weight capacity of knapsack
        weights: List of item weights
        values: List of item values
        
    Returns:
        Maximum value that can be obtained
        
    Time complexity: O(n * capacity) where n = number of items
    Space complexity: O(n * capacity)
    """
    n = len(weights)
    
    # dp[i][w] = maximum value using first i items with weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i - 1][w]
            
            # Take item i-1 if it fits
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    return dp[n][capacity]


def knapsack_01_optimized(capacity, weights, values):
    """
    Space-optimized version using only O(capacity) space.
    """
    n = len(weights)
    
    # Only need previous row
    prev = [0] * (capacity + 1)
    curr = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity + 1):
            # Don't take current item
            curr[w] = prev[w]
            
            # Take current item if it fits
            if weights[i] <= w:
                curr[w] = max(curr[w], prev[w - weights[i]] + values[i])
        
        prev, curr = curr, prev
    
    return prev[capacity]


def knapsack_01_with_items(capacity, weights, values):
    """
    Returns both maximum value and the items taken.
    
    Returns:
        Tuple of (max_value, items_taken)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    # Reconstruct which items were taken
    items_taken = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_taken.append(i - 1)  # 0-indexed item
            w -= weights[i - 1]
    
    items_taken.reverse()
    return dp[n][capacity], items_taken


def knapsack_without_repetition(capacity, weights):
    """
    Find maximum weight that can be achieved without exceeding capacity,
    using each item at most once. This is the discrete knapsack variant.
    """
    n = len(weights)
    
    # dp[w] = True if weight w can be achieved
    dp = [False] * (capacity + 1)
    dp[0] = True
    
    for weight in weights:
        # Traverse backwards to avoid using the same item multiple times
        for w in range(capacity, weight - 1, -1):
            if dp[w - weight]:
                dp[w] = True
    
    # Find maximum achievable weight
    for w in range(capacity, -1, -1):
        if dp[w]:
            return w
    
    return 0


# Input/Output handling for Coursera format
if __name__ == "__main__":
    W, n = map(int, input().split())
    weights = []
    
    for _ in range(n):
        w = int(input())
        weights.append(w)
    
    # For the course version, we want to find maximum weight without repetition
    # This is different from traditional 0/1 knapsack with values
    result = knapsack_without_repetition(W, weights)
    print(result)