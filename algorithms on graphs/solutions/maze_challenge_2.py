def number_of_connected_components_correct(vertices, m):
    """
    Find the number of connected components in a graph.
    
    Args:
        vertices: Dictionary where keys are vertices and values are lists of adjacent vertices
        m: Total number of vertices (nodes) in the graph
    
    Returns:
        Number of connected components
    """
    # Create adjacency list that includes all vertices (even isolated ones)
    adj_list = {i: [] for i in range(1, m + 1)}
    
    # Add edges from the input
    for vertex, neighbors in vertices.items():
        if vertex not in adj_list:
            adj_list[vertex] = []
        for neighbor in neighbors:
            if neighbor not in adj_list:
                adj_list[neighbor] = []
            # Add bidirectional edges
            if neighbor not in adj_list[vertex]:
                adj_list[vertex].append(neighbor)
            if vertex not in adj_list[neighbor]:
                adj_list[neighbor].append(vertex)
    
    visited = set()
    
    def dfs(node):
        """Explore all nodes in the current connected component"""
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    # Count connected components
    num_components = 0
    for vertex in range(1, m + 1):
        if vertex not in visited:
            dfs(vertex)
            num_components += 1
    
    return num_components

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
        vertices[b].append(a)  # Assuming undirected graph
    
    # Print number of connected components
    print(number_of_connected_components_correct(vertices, n))