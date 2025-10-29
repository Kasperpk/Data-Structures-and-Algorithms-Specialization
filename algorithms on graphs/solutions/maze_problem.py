def maze_problem(vertices, u, v, visited_nodes=None):
    """
    Determine if there is a path from vertex u to vertex v in the maze.
    Args:
        vertices (dict): Dictionary representing the maze graph where keys are vertices
                        and values are lists of adjacent vertices
        u (int): Starting vertex
        v (int): Target vertex
        visited_nodes (set): Set of visited vertices (internal use for recursion)
    Returns:
        int: 1 if path exists, 0 if no path exists
    """

     # Create adjacency list that includes all vertices (even isolated ones)
    adj_list = {i: [] for i in range(1, m + 1)}

     # Create adjacency list that includes all vertices (even isolated ones)
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

        for vertex in vertices[u]:
            if vertex not in visited:
                print(visited)
                dfs(vertex)

        if v in visited:
            return 1
        else:
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
        
    # Read vertices to check for path
    u, v = map(int, input().split())
    
    # Print result
    print(maze_problem(vertices, u, v))

