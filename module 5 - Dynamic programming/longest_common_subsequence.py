def longest_common_subsequence(seq1, seq2):
    """
    Find the length of the longest common subsequence between two sequences.
    A subsequence is a sequence that can be derived from another sequence by 
    deleting some or no elements without changing the order of remaining elements.
    
    Args:
        seq1: First sequence (list or string)
        seq2: Second sequence (list or string)
        
    Returns:
        Length of the longest common subsequence
        
    Time complexity: O(len(seq1) * len(seq2))
    Space complexity: O(len(seq1) * len(seq2))
    """
    m, n = len(seq1), len(seq2)
    
    # dp[i][j] = length of LCS of seq1[:i] and seq2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                # Characters match, extend the LCS
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Take maximum from either direction
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def lcs_with_sequence(seq1, seq2):
    """
    Returns both the length and the actual LCS.
    
    Returns:
        Tuple of (length, lcs_sequence)
    """
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()
    return dp[m][n], lcs


def lcs_three_sequences(seq1, seq2, seq3):
    """
    Find the LCS of three sequences using 3D DP.
    
    Time complexity: O(len(seq1) * len(seq2) * len(seq3))
    Space complexity: O(len(seq1) * len(seq2) * len(seq3))
    """
    l1, l2, l3 = len(seq1), len(seq2), len(seq3)
    
    # 3D DP table
    dp = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            for k in range(1, l3 + 1):
                if seq1[i - 1] == seq2[j - 1] == seq3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i][j - 1][k],
                        dp[i][j][k - 1]
                    )
    
    return dp[l1][l2][l3]


# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    if n == 2:
        seq1 = list(map(int, input().split()))
        seq2 = list(map(int, input().split()))
        result = longest_common_subsequence(seq1, seq2)
    else:  # n == 3
        seq1 = list(map(int, input().split()))
        seq2 = list(map(int, input().split()))
        seq3 = list(map(int, input().split()))
        result = lcs_three_sequences(seq1, seq2, seq3)
    
    print(result)