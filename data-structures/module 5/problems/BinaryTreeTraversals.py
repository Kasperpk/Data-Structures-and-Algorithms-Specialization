class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def in_order_traversal(tree, root, res):
    '''
    Input: 
        root: the current node being processed
        tree: the list of nodes making up the tree
        res: list to store the traversal result
    Output: the keys in in-order traversal
    '''
    if root is None:
        return res
    
    # Process left subtree
    if root.left != -1:
        in_order_traversal(tree, tree[root.left], res)
    
    # Process current node
    res.append(root.key)
    
    # Process right subtree
    if root.right != -1:
        in_order_traversal(tree, tree[root.right], res)
    
    return res

def pre_order_traversal(tree, root, res):
    '''
    Input: 
        root: the current node being processed
        tree: the list of nodes making up the tree
        res: list to store the traversal result
    Output: the keys in pre-order traversal
    '''
    if root is None:
        return res
    
    # Process current node
    res.append(root.key)
    
    # Process left subtree
    if root.left != -1:
        pre_order_traversal(tree, tree[root.left], res)
    
    # Process right subtree
    if root.right != -1:
        pre_order_traversal(tree, tree[root.right], res)
    
    return res

def post_order_traversal(tree, root, res):
    '''
    Input: 
        root: the current node being processed
        tree: the list of nodes making up the tree
        res: list to store the traversal result
    Output: the keys in post-order traversal
    '''
    if root is None:
        return res
    
    # Process left subtree
    if root.left != -1:
        post_order_traversal(tree, tree[root.left], res)
    
    # Process right subtree
    if root.right != -1:
        post_order_traversal(tree, tree[root.right], res)
    
    # Process current node
    res.append(root.key)
    
    return res

if __name__ == '__main__':
    # Read the number of nodes
    n = int(input())
    
    # Read node information
    tree = []
    for _ in range(n):
        key, left, right = map(int, input().split())
        node = Node(key)
        node.left = left
        node.right = right
        tree.append(node)
    
    # Perform and print the three traversals
    if n > 0:
        print(' '.join(map(str, in_order_traversal(tree, tree[0], []))))
        print(' '.join(map(str, pre_order_traversal(tree, tree[0], []))))
        print(' '.join(map(str, post_order_traversal(tree, tree[0], []))))
    else:
        print()
        print()
        print()
