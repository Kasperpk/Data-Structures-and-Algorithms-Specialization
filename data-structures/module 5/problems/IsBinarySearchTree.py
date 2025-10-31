class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_binary_search_tree(tree, index, min_val=float('-inf'), max_val=float('inf')):
    """
    Check if tree is a valid BST using min/max bounds approach.
    
    Args:
        tree: List of nodes
        index: Current node index
        min_val: Minimum allowed value for current node
        max_val: Maximum allowed value for current node
    
    Returns:
        True if valid BST, False otherwise
    """
    # Empty tree or reached leaf (-1 index)
    if index == -1:
        return True
    
    node = tree[index]
    
    # Check if current node violates BST property
    if node.key < min_val or node.key >= max_val:
        return False
    
    # Recursively check left and right subtrees
    # Left subtree: all values must be < node.key
    # Right subtree: all values must be >= node.key (allowing duplicates on right)
    return (is_binary_search_tree(tree, node.left, min_val, node.key) and
            is_binary_search_tree(tree, node.right, node.key, max_val))

if __name__ == '__main__':
    n = int(input())
    
    if n == 0:
        print('CORRECT')
    else:
        tree = []
        for _ in range(n):
            key, left, right = map(int, input().split())
            node = Node(key)
            node.left = left
            node.right = right
            tree.append(node)
        
        if is_binary_search_tree(tree, 0):
            print('CORRECT')
        else:
            print('INCORRECT')