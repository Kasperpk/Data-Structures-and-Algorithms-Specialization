def rabin_karp(text, pattern):
    """
    Implementation of Rabin-Karp algorithm for string matching.
    Returns list of positions where pattern occurs in text.
    """
    # Return empty list if either string is empty or pattern longer than text
    if not pattern or not text or len(pattern) > len(text):
        return []
    
    # Variables for hash calculation
    d = 256  # number of characters in input alphabet
    q = 1000000007  # a prime number for hash modulation
    n = len(text)
    m = len(pattern)
    positions = []  # stores all positions where pattern matches
    
    # Calculate hash value for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = pow(d, m-1, q)  # d^(m-1) % q
    
    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q
    
    # Slide pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check character by character
            if text[i:i + m] == pattern:
                positions.append(i)
        
        # Calculate hash value for next window
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            # Make sure hash is positive
            if text_hash < 0:
                text_hash += q
    
    return positions

if __name__ == '__main__':
    # Read input as required by grader
    pattern = input().strip()
    text = input().strip()
    
    # Find all occurrences and print result
    positions = rabin_karp(text, pattern)
    print(' '.join(map(str, positions)))