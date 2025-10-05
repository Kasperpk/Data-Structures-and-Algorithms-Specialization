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
    # Initialize with 0-based indexing
    parent = list(range(n))  # Each table points to itself initially
    size = rows.copy()       # Current size of each table
    max_table_size = max(rows)  # Track maximum size
    
    def find(table):
        # Find set representative with path compression
        # Using 0-based indexing, no need for -1 adjustments
        if table != parent[table]:
            parent[table] = find(parent[table])  # Path compression
        return parent[table]
    
    def union(destination, source):
        nonlocal max_table_size
        
        # Find real representatives of the sets
        real_dest = find(destination - 1)  # Convert to 0-based index
        real_source = find(source - 1)
        
        if real_dest == real_source:
            return max_table_size  # Already merged
        
        # Merge source into destination
        parent[real_source] = real_dest
        
        # Update sizes
        size[real_dest] += size[real_source]
        size[real_source] = 0
        
        # Update maximum size if necessary
        max_table_size = max(max_table_size, size[real_dest])
        
        return max_table_size
    
    # Process all merges and collect results
    result = []
    for dest, source in merges:
        current_max = union(dest, source)
        result.append(current_max)
    
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    rows = list(map(int, input().split()))
    merges = [tuple(map(int, input().split())) for _ in range(m)]

    results = merge_tables(n,m,rows,merges)
    for res in results:
        print(res)