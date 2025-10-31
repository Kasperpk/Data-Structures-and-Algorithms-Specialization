class StringHasher:
    def __init__(self, string, base=263, prime=1000000007):
        self.s = string
        self.base = base
        self.prime = prime
        self._precompute_hashes()
        
    def _precompute_hashes(self):
        """Precompute hash values for all prefixes of the string"""
        self.hash_values = [0] * (len(self.s) + 1)
        self.powers = [1] * (len(self.s) + 1)
        
        # Compute powers
        for i in range(1, len(self.s) + 1):
            self.powers[i] = (self.powers[i-1] * self.base) % self.prime
            
        # Compute hash values
        for i in range(1, len(self.s) + 1):
            self.hash_values[i] = (self.hash_values[i-1] * self.base + 
                                 ord(str(self.s[i-1]))) % self.prime

    def get_hash(self, start, length):
        """Get hash value for substring of given length starting at start"""
        h = (self.hash_values[start + length] - 
             self.hash_values[start] * self.powers[length]) % self.prime
        if h < 0:
            h += self.prime
        return h

def find_common_subsequence(n, m, a, b):
    # Convert arrays to strings with special delimiter to avoid collisions
    str_a = ' '.join(map(str, a))
    str_b = ' '.join(map(str, b))
    
    # Create hashers for both strings
    hasher_a = StringHasher(str_a)
    hasher_b = StringHasher(str_b)
    
    # Find equal elements
    result = []
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                # Check if elements are part of a longer sequence
                len_a = len(str(a[i]))
                len_b = len(str(b[j]))
                hash_a = hasher_a.get_hash(i * 2, len_a)  # *2 because of spaces
                hash_b = hasher_b.get_hash(j * 2, len_b)
                if hash_a == hash_b:
                    result.append(a[i])
                    break
    
    return result

if __name__ == '__main__':
    # Read input
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    # Find the common subsequence
    result = find_common_subsequence(n, m, a, b)
    
    # Print the result
    print(*result)
