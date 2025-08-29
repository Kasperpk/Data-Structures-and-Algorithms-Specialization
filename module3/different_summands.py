def max_number_of_prizes(n):
    """
    Represent a positive integer n as a sum of as many distinct positive integers as possible.
    
    Uses greedy algorithm: use smallest possible distinct positive integers,
    adjusting the last one to make the sum exactly n.
    """
    if n == 1:
        return [1]
    
    summands = []
    current = 1
    remaining = n
    
    while remaining > 0:
        if remaining - current > current:
            # We can safely add 'current' and still have room for the next distinct number
            summands.append(current)
            remaining -= current
            current += 1
        else:
            # Add the remaining amount to the last summand to make sum exactly n
            summands.append(remaining)
            remaining = 0
    
    return summands

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    summands = max_number_of_prizes(n)
    
    print(len(summands))
    print(' '.join(map(str, summands)))