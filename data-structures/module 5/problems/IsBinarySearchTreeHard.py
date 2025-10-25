class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def in_order_traversal(tree, index, result):
    """Perform in-order traversal and collect keys."""
    if index == -1:
        return
    
    node = tree[index]
    in_order_traversal(tree, node.left, result)
    result.append(node.key)
    in_order_traversal(tree, node.right, result)

def is_binary_search_tree(tree):
    """
    Check if tree is a valid BST using in-order traversal.
    For the hard version, duplicates are allowed and should be handled.
    A valid BST's in-order traversal should be sorted (non-decreasing).
    """
    if not tree:
        return True
    
    result = []
    in_order_traversal(tree, 0, result)
    
    # Check if the in-order traversal is sorted (non-decreasing for hard version)
    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            return False
    
    return True

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
        
        if is_binary_search_tree(tree):
            print('CORRECT')
        else:
            print('INCORRECT')