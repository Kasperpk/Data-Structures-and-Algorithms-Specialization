def topological_sort(vertices):
    """
    Perform topological sort on a directed acyclic graph (DAG).
    Returns a valid ordering of vertices such that for every directed edge u->v, 
    u comes before v in the ordering.
    
    Args:
        vertices: Dictionary representing adjacency list {vertex: [neighbors]}
    
    Returns:
        List of vertices in topological order
        
    Time complexity: O(V + E)
    Space complexity: O(V)
    """
    visited = set()
    order = []
    
    def dfs(vertex):
        """DFS to explore graph and add vertices in post-order"""
        visited.add(vertex)
        
        # Visit all neighbors first
        for neighbor in vertices.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        
        # Add vertex to order after visiting all descendants (post-order)
        order.append(vertex)
    
    # Visit all vertices
    for vertex in vertices:
        if vertex not in visited:
            dfs(vertex)
    
    # Reverse to get topological order (post-order reversed)
    return order[::-1]


if __name__ == '__main__':
    # Read number of vertices (n) and edges (m)
    n, m = map(int, input().split())
    
    # Initialize vertices dictionary
    vertices = {i: [] for i in range(1, n + 1)}
    
    # Read m edges
    for _ in range(m):
        # Read edge vertices a, b (a must come before b)
        a, b = map(int, input().split())
        vertices[a].append(b)
    
    # Get topological order
    result = topological_sort(vertices)
    
    # Print result as space-separated values
    print(' '.join(map(str, result)))
