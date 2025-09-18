def edit_distance(str1, str2):
    """
    Compute the edit distance (Levenshtein distance) between two strings.
    Edit distance is the minimum number of operations (insertions, deletions, 
    substitutions) required to change one string into the other.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        Minimum edit distance between the strings
        
    Time complexity: O(len(str1) * len(str2))
    Space complexity: O(len(str1) * len(str2))
    """
    m, n = len(str1), len(str2)
    
    # dp[i][j] = edit distance between str1[:i] and str2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: converting from/to empty string
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from str1
    
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters from str2
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Choose minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Substitution
                )
    
    return dp[m][n]


def edit_distance_optimized(str1, str2):
    """
    Space-optimized version using only O(min(len(str1), len(str2))) space.
    """
    # Ensure str1 is the shorter string for space optimization
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    m, n = len(str1), len(str2)
    
    # Only need previous and current row
    prev = list(range(m + 1))
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        curr[0] = j
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[i] = prev[i - 1]
            else:
                curr[i] = 1 + min(prev[i], curr[i - 1], prev[i - 1])
        prev, curr = curr, prev
    
    return prev[m]


# Input/Output handling for Coursera format
if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    result = edit_distance(str1, str2)
    print(result)