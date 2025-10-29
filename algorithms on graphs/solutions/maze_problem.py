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
    # Initialize visited_nodes on first call
    if visited_nodes is None:
        visited_nodes = set()

    # If we've reached the target vertex directly, path found
    if v in vertices[u]:
        return 1
    
    # Mark current node visited to avoid maximum recursion
    visited_nodes.add(u)
    
    # check all adjacent vertices
    for next_vertex in vertices[u]:
        if next_vertex in visited_nodes:
            continue
        else:
            # Recursively check if we can reach target from this vertex
            if maze_problem(vertices=vertices, u=next_vertex, v=v, visited_nodes=visited_nodes) == 1:
                return 1
        
    # No path found from this vertex
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