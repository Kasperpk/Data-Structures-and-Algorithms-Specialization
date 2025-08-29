def max_dot_product(prices, clicks):
    """
    Maximize the total revenue from advertisement.
    Revenue = sum of (price_i * clicks_i) for matched advertisements.
    
    Uses greedy algorithm: sort both arrays and pair largest with largest.
    """
    # Sort both arrays in descending order
    prices.sort(reverse=True)
    clicks.sort(reverse=True)
    
    total_revenue = 0
    n = len(prices)
    
    for i in range(n):
        total_revenue += prices[i] * clicks[i]
    
    return total_revenue

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    
    result = max_dot_product(prices, clicks)
    print(result)