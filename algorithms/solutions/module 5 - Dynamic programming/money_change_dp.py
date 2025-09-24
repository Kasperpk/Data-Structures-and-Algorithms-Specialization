def money_change_dp(money, coins):
    """
    Find the minimum number of coins needed to change the given amount of money
    using dynamic programming. This version can handle any coin denominations,
    unlike the greedy algorithm which only works for certain coin systems.
    
    Args:
        money: Amount of money to change
        coins: List of coin denominations available
        
    Returns:
        Minimum number of coins needed
        
    Time complexity: O(money * len(coins))
    Space complexity: O(money)
    """
    # dp[i] = minimum number of coins needed to make amount i
    dp = [float('inf')] * (money + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
    for amount in range(1, money + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[money] if dp[money] != float('inf') else -1


def money_change_standard(money):
    """
    Standard version using coins [1, 3, 4] as typically used in coursework.
    """
    return money_change_dp(money, [1, 3, 4])


# Input/Output handling for Coursera format
if __name__ == "__main__":
    money = int(input())
    result = money_change_standard(money)
    print(result)