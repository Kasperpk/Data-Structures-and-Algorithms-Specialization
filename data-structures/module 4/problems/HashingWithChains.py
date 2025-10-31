class HashTableWithChain:
    def __init__(self, buckets):
        """Initialize hash table with given number of buckets"""
        self.buckets = buckets
        self.hash_table = {}
        for bucket in range(0, self.buckets):
            self.hash_table[bucket] = []
        self.x = 263
        self.prime = 1000000007

    def compute_hash(self, string):
        """Compute polynomial hash value for a string"""
        ans = 0
        for c in string:
            ans = (ans * self.x + ord(c)) % self.prime
        return ans % self.buckets

    def add_string(self, query):
        """Add a string to the hash table if it's not already there"""
        string = query.split()[1]  # get the string part from the query
        hash_value = self.compute_hash(string)
        if string not in self.hash_table[hash_value]:
            self.hash_table[hash_value].append(string)  # append at end of chain

    def check(self, query):
        """Print all strings in given chain, in reverse order of insertion"""
        i = int(query.split()[1])  # get the index from query
        if 0 <= i < self.buckets:
            # Print chain in reverse order
            chain = self.hash_table[i]
            if chain:
                print(' '.join(reversed(chain)))
            else:
                print()
        else:
            print()

    def find(self, query):
        """Check if a string exists in the hash table"""
        string = query.split()[1]  # get the string part from the query
        hash_value = self.compute_hash(string)
        print('yes' if string in self.hash_table[hash_value] else 'no')

    def delete_string(self, query):
        """Delete a string from the hash table if it exists"""
        string = query.split()[1]  # get the string part from the query
        hash_value = self.compute_hash(string)
        if string in self.hash_table[hash_value]:
            self.hash_table[hash_value].remove(string)

def process_queries():
    # Read the number of buckets
    m = int(input())
    # Read the number of queries
    n = int(input())
    
    # Create hash table
    hash_table = HashTableWithChain(m)
    
    # Process each query
    for _ in range(n):
        query = input().strip()
        if query.startswith('add'):
            hash_table.add_string(query)
        elif query.startswith('del'):
            hash_table.delete_string(query)
        elif query.startswith('find'):
            hash_table.find(query)
        elif query.startswith('check'):
            hash_table.check(query)

if __name__ == '__main__':
    process_queries()