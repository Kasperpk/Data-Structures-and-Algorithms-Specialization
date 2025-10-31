class Rope:
    """
    Rope data structure for efficient string manipulation.
    Uses a simple string-based approach for the Coursera problem.
    """
    
    def __init__(self, s):
        """Initialize rope with string s."""
        self.s = s
    
    def process(self, i, j, k):
        """
        Cut substring from position i to j (inclusive) and insert at position k.
        
        Args:
            i: Start position of cut (0-indexed)
            j: End position of cut (0-indexed, inclusive)
            k: Position to insert the cut substring
        """
        # Extract the substring to cut
        cut_str = self.s[i:j+1]
        
        # Remove the cut substring from original string
        remaining = self.s[:i] + self.s[j+1:]
        
        # Insert the cut substring at position k
        self.s = remaining[:k] + cut_str + remaining[k:]
    
    def result(self):
        """Return the final string."""
        return self.s


if __name__ == '__main__':
    s = input().strip()
    q = int(input())
    
    rope = Rope(s)
    
    for _ in range(q):
        i, j, k = map(int, input().split())
        rope.process(i, j, k)
    
    print(rope.result())
