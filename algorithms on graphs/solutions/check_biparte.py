"""
Coursera: Data Structures and Algorithms Specialization
Problem: Checking whether a Graph is Bipartite

A graph is bipartite if its vertices can be split into two parts such that
each edge joins vertices from different parts. Equivalently, vertices can be
colored with two colors such that no adjacent vertices have the same color.

Algorithm: BFS-based 2-coloring
- Try to color the graph with two colors using BFS
- If we find an edge connecting two vertices of the same color, it's not bipartite
- Handle disconnected graphs by checking all components

Key insight: A graph is bipartite if and only if it contains no odd-length cycles
"""


def is_bipartite(n, adj):
    """
    Check if an undirected graph is bipartite using BFS coloring.
    
    A graph is bipartite if its vertices can be colored with two colors
    such that no two adjacent vertices have the same color.
    
    Args:
        n: Number of vertices (1 to n)
        adj: Adjacency list representing the graph
    
    Returns:
        1 if bipartite, 0 otherwise
        
    Time complexity: O(V + E)
    Space complexity: O(V)
    """
    # Color array: -1 = uncolored, 0 = color 0, 1 = color 1
    color = [-1] * (n + 1)
    
    # Check all components (graph might be disconnected)
    for start in range(1, n + 1):
        if color[start] == -1:
            # BFS to color this component
            queue = [start]
            color[start] = 0
            
            while queue:
                vertex = queue.pop(0)
                current_color = color[vertex]
                
                for neighbor in adj[vertex]:
                    if color[neighbor] == -1:
                        # Neighbor not colored yet, color with opposite color
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Neighbor has same color - not bipartite
                        return 0
    
    return 1


if __name__ == "__main__":
    # Read number of vertices and edges
    n, m = map(int, input().split())
    
    # Initialize adjacency list for vertices 1 to n
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if bipartite and print result
    print(is_bipartite(n, adj))