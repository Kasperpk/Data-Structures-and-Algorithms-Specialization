def placing_parentheses(expression):
    """
    Maximize the value of an arithmetic expression by placing parentheses.
    The expression consists of digits and operations (+, -, *).
    
    Args:
        expression: String containing digits and operators alternating
        
    Returns:
        Maximum possible value of the expression
        
    Time complexity: O(n^3) where n is the number of operands
    Space complexity: O(n^2)
    """
    # Parse the expression into numbers and operators
    numbers = []
    operators = []
    
    for i, char in enumerate(expression):
        if i % 2 == 0:  # Even indices are numbers
            numbers.append(int(char))
        else:  # Odd indices are operators
            operators.append(char)
    
    n = len(numbers)
    if n == 1:
        return numbers[0]
    
    # dp_max[i][j] = maximum value of subexpression from numbers[i] to numbers[j]
    # dp_min[i][j] = minimum value of subexpression from numbers[i] to numbers[j]
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]
    
    # Base case: single numbers
    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]
    
    # Fill the DP table for increasing lengths
    for length in range(2, n + 1):  # length of subexpression
        for i in range(n - length + 1):
            j = i + length - 1
            
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            
            # Try all possible split points
            for k in range(i, j):
                operator = operators[k]
                
                # Calculate all possible values at split point k
                a = dp_max[i][k]
                b = dp_max[k + 1][j]
                c = dp_min[i][k]
                d = dp_min[k + 1][j]
                
                values = [
                    calculate(a, b, operator),
                    calculate(a, d, operator),
                    calculate(c, b, operator),
                    calculate(c, d, operator)
                ]
                
                dp_max[i][j] = max(dp_max[i][j], max(values))
                dp_min[i][j] = min(dp_min[i][j], min(values))
    
    return dp_max[0][n - 1]


def calculate(a, b, operator):
    """Helper function to perform arithmetic operations."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        raise ValueError(f"Unknown operator: {operator}")


def placing_parentheses_memoization(expression):
    """
    Alternative implementation using memoization (top-down approach).
    """
    numbers = []
    operators = []
    
    for i, char in enumerate(expression):
        if i % 2 == 0:
            numbers.append(int(char))
        else:
            operators.append(char)
    
    n = len(numbers)
    memo_max = {}
    memo_min = {}
    
    def dp(i, j):
        """Returns (max_value, min_value) for subexpression from i to j."""
        if i == j:
            return numbers[i], numbers[i]
        
        if (i, j) in memo_max:
            return memo_max[(i, j)], memo_min[(i, j)]
        
        max_val = float('-inf')
        min_val = float('inf')
        
        for k in range(i, j):
            operator = operators[k]
            
            left_max, left_min = dp(i, k)
            right_max, right_min = dp(k + 1, j)
            
            values = [
                calculate(left_max, right_max, operator),
                calculate(left_max, right_min, operator),
                calculate(left_min, right_max, operator),
                calculate(left_min, right_min, operator)
            ]
            
            max_val = max(max_val, max(values))
            min_val = min(min_val, min(values))
        
        memo_max[(i, j)] = max_val
        memo_min[(i, j)] = min_val
        
        return max_val, min_val
    
    max_result, _ = dp(0, n - 1)
    return max_result


# Input/Output handling for Coursera format
if __name__ == "__main__":
    expression = input().strip()
    result = placing_parentheses(expression)
    print(result)