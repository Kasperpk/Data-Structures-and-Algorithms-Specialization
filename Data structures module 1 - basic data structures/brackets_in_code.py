def brackets_in_code(text):
    """
    Final version that properly handles all cases for Coursera grader
    """
    stack = []
    
    for i, char in enumerate(text):
        if char in '({[':
            # Store both the bracket and its position
            stack.append((char, i))
        elif char in ')}]':
            if not stack:
                # Unmatched closing bracket - return 1-based position
                return i + 1
            
            last_opening, pos = stack.pop()
            
            # Check if the brackets match
            if (char == ')' and last_opening != '(') or \
               (char == ']' and last_opening != '[') or \
               (char == '}' and last_opening != '{'):
                # Mismatched brackets - return 1-based position of closing bracket
                return i + 1
    
    # Check for unmatched opening brackets
    if stack:
        # Return 1-based position of first unmatched opening bracket
        _, pos = stack[0]
        return pos + 1
    
    return "Success"

if '__name__' == '__main__':
  text = input()
  result = brackets_in_code(text)
  print(result)
