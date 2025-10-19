class Node:

    def __init__(self, key):

        self.key = key
        self.left = None
        self.right = None

def in_order_traversal(tree,root,res):
    '''
    Input: 
        r the root node of the tree
        tree the list of nodes making up the tree
    Output the keys in-order traversal
    '''
    if root.left == -1 and root.right == -1:
        if root.key not in res:
            res.append(root.key)
        return 
    

    in_order_traversal(tree, tree[root.left],res)
    if root.key not in res:
        res.append(root.key)
    in_order_traversal(tree, tree[root.right],res)
    if root.key not in res:
        res.append(root.key)
    return res

def pre_order_traversal(tree, root,res):


    if root.left == -1 and root.right == -1:
        if root.key not in res:
            res.append(root.key)
        return 

    
    res.append(root.key)
    pre_order_traversal(tree, tree[root.left], res)
    
    pre_order_traversal(tree, tree[root.right],res)

    return res

def post_order_traversal(tree, root, res):

    if root.left == -1 and root.right == -1:
        if root.key not in res:
            res.append(root.key)
        return
    
    post_order_traversal(tree, tree[root.left], res)
    post_order_traversal(tree, tree[root.right], res)

    res.append(root.key)

    return res



if __name__ == '__main__':
    
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(0,n)]

    tree = []

    for line in lines:
        node = Node(line[0])
        node.left = line[1]
        node.right = line[2]
        tree.append(node)
    

    in_ord = in_order_traversal(tree, tree[0], res=[])
    print(in_ord)
    pre_ord = pre_order_traversal(tree, tree[0], res=[])
    print(pre_ord)
    post_ord = post_order_traversal(tree, tree[0], res=[])
    print(post_ord)
