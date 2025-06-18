class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from problems import max_depth_binary_tree, same_tree, invert_binary_tree

def test_max_depth_binary_tree():
    # Test case 1: Empty tree
    root = None
    assert max_depth_binary_tree(root) == 0
    
    # Test case 2: Single node tree
    root = TreeNode(1)
    assert max_depth_binary_tree(root) == 1
    
    # Test case 3: Balanced binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert max_depth_binary_tree(root) == 3
    
    print("All test cases passed!")

def test_same_tree():
    # Test case 1: Empty trees
    p = None
    q = None
    assert same_tree(p, q) == True
    
    # Test case 2: Single node trees
    p = TreeNode(1)
    q = TreeNode(1)
    assert same_tree(p, q) == True
    
    # Test case 3: Different trees
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(4)
    assert same_tree(p, q) == False
    
    print("All test cases passed!")

def test_invert_binary_tree():
    # Test case 1: Empty tree
    root = None
    assert invert_binary_tree(root) == None
    
    # Test case 2: Single node tree
    root = TreeNode(1)
    inverted = invert_binary_tree(root)
    assert inverted.val == 1
    
    # Test case 3: Balanced binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    inverted = invert_binary_tree(root)
    assert inverted.val == 1
    assert inverted.left.val == 3
    assert inverted.right.val == 2
    assert inverted.right.left.val == 5
    assert inverted.right.right.val == 4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_depth_binary_tree()
    test_same_tree()
    test_invert_binary_tree()
