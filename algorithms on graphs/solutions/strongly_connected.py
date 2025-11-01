def is_strongly_connected(vertices, n):
    """
    Check if a directed graph is strongly connected.
    A graph is strongly connected if there is a path from any vertex to any other vertex.
    
    Uses Kosaraju's algorithm:
    1. Do DFS from any vertex and check if all vertices are reachable
    2. Reverse the graph
    3. Do DFS again from the same vertex
    4. If all vertices are reachable in both passes, graph is strongly connected
    
    Args:
        vertices: Dictionary representing adjacency list {vertex: [neighbors]}
        n: Number of vertices
    
    Returns:
        1 if strongly connected, 0 otherwise
        
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    """
    if n == 0:
        return 1
    
    # Find a vertex that exists in the graph (for graphs with isolated vertices)
    start_vertex = 1
    
    def dfs(graph, start, visited):
        """Perform DFS and mark all reachable vertices"""
        visited.add(start)
        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
    
    # First DFS from start_vertex
    visited1 = set()
    dfs(vertices, start_vertex, visited1)
    
    # If not all vertices are reachable from start_vertex, not strongly connected
    if len(visited1) != n:
        return 0
    
    # Create reversed graph
    reversed_vertices = {i: [] for i in range(1, n + 1)}
    for vertex in vertices:
        for neighbor in vertices[vertex]:
            reversed_vertices[neighbor].append(vertex)
    
    # Second DFS on reversed graph from the same start_vertex
    visited2 = set()
    dfs(reversed_vertices, start_vertex, visited2)
    
    # If all vertices are reachable in reversed graph, then strongly connected
    if len(visited2) != n:
        return 0
    
    return 1


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
    print(is_strongly_connected(vertices, n))
