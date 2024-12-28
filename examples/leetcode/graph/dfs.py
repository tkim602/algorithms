# Binary Tree Inorder Traversal (Leetcode #94 - easy)
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example: 
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left
            
            root = st.pop()
            res.append(root.val)

            root = root.right
        
        return res   

# root: the root node of the binary tree
# Optional[TreeNode]: it tells that the root can be None

# First, initialize variables, 2 stacks, one to store nodes during traversal and the other to store the values of the nodes in inorder sequence 

# Using the while loop, the inner loop keeps traversing down the left subtree, adding each node to the stack.
# It reaches the leftmost node of the current subtree.

# Once the leftmost node is reached, the node is popped from the stack and its value is added to the result list. 
# Then, the traversal moves to the node's right child, if exists

# The time complexity of the algorithm is O(n), where n is the number of nodes in the binary tree.
# O(n) (outer loop) + O(n) (inner loop) + O(n) (appending the value of a node to res list O(1) * n)

# cont. (med and hard) 
        

