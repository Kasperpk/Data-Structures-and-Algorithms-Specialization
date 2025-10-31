class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263
        self.h1 = self._precompute_hashes(self.m1)
        self.h2 = self._precompute_hashes(self.m2)
        self.pow1 = self._precompute_powers(self.m1)
        self.pow2 = self._precompute_powers(self.m2)

    def _precompute_hashes(self, m):
        """Precompute hashes for all prefixes of the string"""
        h = [0] * (len(self.s) + 1)
        for i in range(1, len(self.s) + 1):
            h[i] = (h[i-1] * self.x + ord(self.s[i-1])) % m
        return h

    def _precompute_powers(self, m):
        """Precompute powers of x"""
        powers = [1] * (len(self.s) + 1)
        for i in range(1, len(self.s) + 1):
            powers[i] = (powers[i-1] * self.x) % m
        return powers

    def ask(self, a, b, l):
        """Check if substrings are equal using precomputed hashes"""
        # Get hash1 for first substring
        h1_a = (self.h1[a+l] - (self.h1[a] * self.pow1[l]) % self.m1) % self.m1
        if h1_a < 0:
            h1_a += self.m1
            
        # Get hash1 for second substring
        h1_b = (self.h1[b+l] - (self.h1[b] * self.pow1[l]) % self.m1) % self.m1
        if h1_b < 0:
            h1_b += self.m1
            
        # Get hash2 for first substring
        h2_a = (self.h2[a+l] - (self.h2[a] * self.pow2[l]) % self.m2) % self.m2
        if h2_a < 0:
            h2_a += self.m2
            
        # Get hash2 for second substring
        h2_b = (self.h2[b+l] - (self.h2[b] * self.pow2[l]) % self.m2) % self.m2
        if h2_b < 0:
            h2_b += self.m2
            
        return h1_a == h1_b and h2_a == h2_b

if __name__ == '__main__':
    # Read the input string
    s = input()
    # Create instance of Solver
    solver = Solver(s)
    # Read number of queries
    n_queries = int(input())
    
    # Process each query
    for _ in range(n_queries):
        a, b, l = map(int, input().split())
        print('Yes' if solver.ask(a, b, l) else 'No')