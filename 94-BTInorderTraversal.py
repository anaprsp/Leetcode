# Recursive
# Time Complexity O(n), where n is the number of nodes. (T(n) = 2T(n/2)) + 1)
# Space Complexity O(n), worst case, and O(log(n)), average case.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        treeList = []
        self.dfs(root, treeList)
        return treeList

    def dfs(self, node, treeList):
        if node:
            self.dfs(node.left, treeList)
            treeList.append(node.val)
            self.dfs(node.right, treeList)

# Iterative
# Time Complexity O(n), where n is the number of nodes
# Space Complexity O(n)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or len(stack):
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
