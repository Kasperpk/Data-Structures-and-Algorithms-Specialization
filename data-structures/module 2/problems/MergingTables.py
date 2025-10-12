def merge_tables(n, m, rows, merges):
    """
    Merge tables and track maximum size.
    Args:
        n: number of tables
        m: number of merge operations
        rows: list of initial table sizes
        merges: list of tuples (destination, source) for merge operations
    Returns:
        list of maximum table sizes after each merge operation
    """
    # Initialize disjoint set data structure
    parent = list(range(n))  # Each table points to itself initially
    rank = [0] * n          # Rank for union by rank optimization
    size = rows.copy()      # Current size of each table
    max_size = max(rows)    # Track maximum size
    
    def find(i):
        """Find set representative with path compression"""
        if i != parent[i]:
            parent[i] = find(parent[i])  # Path compression
        return parent[i]
    
    def merge(destination, source):
        """
        Merge source table into destination table.
        Returns the current maximum table size.
        """
        nonlocal max_size
        
        # Convert to 0-based indexing and find real representatives
        dest_id = find(destination - 1)
        src_id = find(source - 1)
        
        # If tables are already in same set, no merge needed
        if dest_id == src_id:
            return max_size
            
        # Merge smaller rank tree into larger rank tree
        if rank[dest_id] > rank[src_id]:
            parent[src_id] = dest_id
            size[dest_id] += size[src_id]
            size[src_id] = 0
        else:
            parent[dest_id] = src_id
            size[src_id] += size[dest_id]
            size[dest_id] = 0
            if rank[dest_id] == rank[src_id]:
                rank[src_id] += 1
                
        # Update maximum size
        max_size = max(max_size, size[src_id], size[dest_id])
        return max_size
    
    # Process all merge operations
    result = []
    for dest, source in merges:
        max_after_merge = merge(dest, source)
        result.append(max_after_merge)
        
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    rows = list(map(int, input().split()))
    merges = [tuple(map(int, input().split())) for _ in range(m)]

    results = merge_tables(n,m,rows,merges)
    for res in results:
        print(res)