def tree_height(nodes, parents):
    '''
    Calculate the height of a tree given parent array representation
    
    Args:
        n: number of nodes
        parents: array where parents[i] is the parent of node i, -1 for root
    
    Returns:
        Height of the tree (number of edges in longest path from root to leaf)
    '''

    children = [[] for _ in range(nodes)]

    root = -1 

    for i in range(nodes):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)
                           
    def dfs(node):
        if not children[node]:
            return 0
        max_child_height = 0
        for child in children[node]:
            max_child_height = max(max_child_height, dfs(child))

        return max_child_height + 1 

    return dfs(root)
if '__name__' == '__main__':
    nodes = int(input())
    parents = list(map(int, intput().split()))
