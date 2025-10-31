def check_consistency_of_cs(vertices):
    """
    Check if a directed graph contains a cycle using DFS.
    Returns 1 if cycle exists (inconsistent), 0 otherwise (acyclic/consistent).
    
    Args:
        vertices: Dictionary representing adjacency list {vertex: [neighbors]}
    
    Returns:
        1 if cycle detected, 0 if acyclic
    """
    # Track visited nodes and nodes in current recursion stack
    visited = set()
    rec_stack = set()
    
    def has_cycle_dfs(vertex):
        """DFS helper to detect cycle from given vertex"""
        visited.add(vertex)
        rec_stack.add(vertex)
        
        # Check all neighbors
        for neighbor in vertices.get(vertex, []):
            # If neighbor not visited, recurse
            if neighbor not in visited:
                if has_cycle_dfs(neighbor):
                    return True
            # If neighbor is in current recursion stack, cycle found
            elif neighbor in rec_stack:
                return True
        
        # Remove from recursion stack before returning
        rec_stack.remove(vertex)
        return False
    
    # Check from each unvisited vertex
    for vertex in vertices:
        if vertex not in visited:
            if has_cycle_dfs(vertex):
                return 1
    
    return 0


if __name__ == '__main__':
    # Read number of vertices (n) and edges (m)
    n, m = map(int, input().split())
    
    # Initialize vertices dictionary
    vertices = {i: [] for i in range(1, n + 1)}
    
    # Read m edges
    for _ in range(m):
        # Read edge vertices a, b
        a, b = map(int, input().split())
        vertices[a].append(b)
    
    # Print result
    print(check_consistency_of_cs(vertices))