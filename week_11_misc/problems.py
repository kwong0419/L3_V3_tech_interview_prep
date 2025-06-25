# 1. Lowest Common Ancestor
# 2. Serialize and Deserialize Binary Tree
# 3. Course Schedule (Graph Bonus)

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree

def serialize_binary_tree(root):
    if not root:
        return "None"
    return f"{root.val},{serialize_binary_tree(root.left)},{serialize_binary_tree(root.right)}"
# Time Complexity: O(n)
# Space Complexity: O(n)

def deserialize_binary_tree(data):
    def helper(data):
        if data[0] == "None":
            data.pop(0)
            return None
        root = TreeNode(data[0])
        data.pop(0)
        root.left = helper(data)
        root.right = helper(data)
        return root 
    data = data.split(",")
    return helper(data)
# Time Complexity: O(n)
# Space Complexity: O(n)  


