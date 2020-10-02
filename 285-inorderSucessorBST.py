#time complexity O(H). where H is the tree's hight. If the tree were a Binary Tree, then the space complexity would be O(log(n)).
#space complexity O(n), n is the number of nodes in root
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left   
            root = stack.pop()
            if inorder == p.val:    
                return root         
            inorder = root.val
            root = root.right
        return None
