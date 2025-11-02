"""
Coursera: Data Structures and Algorithms Specialization
Problem: Computing the Minimum Number of Flight Segments

Find the shortest path between two vertices in an undirected graph.
This is the minimum number of edges needed to go from vertex u to vertex v.

Algorithm: Breadth-First Search (BFS)
- BFS explores vertices level by level from the source
- The first time we reach a vertex, we've found the shortest path to it
- Use a queue to process vertices in order

Time Complexity: O(V + E)
Space Complexity: O(V)
"""


def bfs_shortest_path(n, adj, start, end):
    """
    Compute shortest path length between start and end vertices using BFS.
    
    Args:
        n: Number of vertices
        adj: Adjacency list representing the graph
        start: Starting vertex
        end: Ending vertex
    
    Returns:
        Length of shortest path, or -1 if no path exists
    """
    if start == end:
        return 0
    
    # Distance array: -1 means not visited yet
    distance = [-1] * (n + 1)
    distance[start] = 0
    
    # BFS queue
    queue = [start]
    
    while queue:
        current = queue.pop(0)
        
        # Explore all neighbors
        for neighbor in adj[current]:
            if distance[neighbor] == -1:
                # First time visiting this vertex
                distance[neighbor] = distance[current] + 1
                
                # Check if we reached the destination
                if neighbor == end:
                    return distance[end]
                
                queue.append(neighbor)
    
    # If we finish BFS without reaching end, no path exists
    return -1


if __name__ == "__main__":
    # Read number of vertices and edges
    n, m = map(int, input().split())
    
    # Initialize adjacency list for vertices 1 to n
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges (undirected graph)
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # Read start and end vertices
    start, end = map(int, input().split())

    # Compute and print shortest path length
    print(bfs_shortest_path(n, adj, start, end))