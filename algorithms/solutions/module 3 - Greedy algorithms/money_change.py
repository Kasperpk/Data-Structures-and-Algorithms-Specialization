def money_change(money):
    """
    Find the minimum number of coins needed to change the given amount of money
    using coins of denominations 1, 5, and 10.
    
    Uses greedy algorithm: always take the largest coin possible.
    """
    coins = [10, 5, 1]  # Coin denominations in descending order
    num_coins = 0
    
    for coin in coins:
        num_coins += money // coin  # Add number of coins of this denomination
        money %= coin  # Update remaining money
    
    return num_coins

# Input/Output handling for Coursera format
if __name__ == "__main__":
    money = int(input())
    result = money_change(money)
    print(result)