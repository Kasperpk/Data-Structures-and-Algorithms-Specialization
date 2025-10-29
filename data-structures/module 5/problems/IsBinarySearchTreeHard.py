class Node:

    def __init__(self, key):

        self.key = key
        self.left = None
        self.right = None

def is_binary_search_tree(tree,root,bst=True):

    # if leaf node is reached then return
    if root.left == -1 and root.right == -1:
        return
    
    # if both child nodes are not -1 then check if BST condition is met
    if root.left != -1 and root.right != -1:
        bst = tree[root.left].key < root.key and tree[root.right].key >= root.key
    
    # if only right node is not leaf check BST condition on that
    elif root.left == -1 and root.right != -1:
        bst = tree[root.right].key >= root.key
    
    # if only left condition check BST condition on that
    elif root.left != -1 and root.right == -1:
        bst = tree[root.left].key < root.key

    # if any of the bst is false return Incorrect  
    if bst == False:
        return print("INCORRECT")
    
    # else recursively call the child nodes
    is_binary_search_tree(tree, tree[root.left], bst)
    is_binary_search_tree(tree, tree[root.right], bst)

    return bst

if __name__ == '__main__':
    
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(0,n)]

    tree = []

    for line in lines:
        node = Node(line[0])
        node.left = line[1]
        node.right = line[2]
        tree.append(node)
    

    result = is_binary_search_tree(tree, tree[0])
    if result == True:
        print('CORRECT')
    else:
        print("INCORRECT")
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