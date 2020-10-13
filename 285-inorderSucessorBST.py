# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#         # Optimization to find the successor node inside the p subtree, since p has right-child.
#         if p.right:
#             p = p.right
#             while p.left:
#                 p = p.left
#             return p

#         stack, inorder = [], float('-inf')

#         # "inorder" stores the node values before exploring the right-child subtree (and stores the largest value of 
#         # the left-child subtree before exploring the node)
#         # "stack" stores the parents chain
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             if inorder == p.val:
#                 return root
#             inorder = root.val
#             root = root.right
#         return None

# time complexity O(H). where H is the tree's hight
# space complexity O(1)
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        parent = None
        while root:
            if root.val > p.val:
                parent = root
                root = root.left
            else:
                root = root.right
        return parent
