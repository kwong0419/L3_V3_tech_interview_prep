### Problems:
# 1. Maximum Depth of Binary Tree
# 2. Same Tree
# 3. Invert Binary Tree

def max_depth_binary_tree(root):
    if not root: # base case - empty node
        return 0
    return 1 + max(max_depth_binary_tree(root.left), max_depth_binary_tree(root.right))
# Time Complexity: O(n) 
# Space Complexity: O(h) where h is the height of the tree

def same_tree(p, q):
    if not p and not q: # both empty nodes
        return True
    if not p or not q: # one empty node, one isn't
        return False
    if p.val != q.val: # different values
        return False
    # check left and right subtrees
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)
# Time Complexity: O(n) 
# Space Complexity: O(h) where h is the height of the tree

def invert_binary_tree(root):
    if not root: # base case - empty node
        return None
    # swap left and right subtrees
    root.left, root.right = root.right, root.left
    # recursively invert left and right subtrees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root
# Time Complexity: O(n) 
# Space Complexity: O(h) where h is the height of the tree
