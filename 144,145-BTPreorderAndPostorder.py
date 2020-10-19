# Preorder Recursive
class Solution:
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		res = []
		self.dfs(root, res)
		return res

	def dfs(self, node, res):
		if node:
			res.append(node.val)
			self.dfs(node.left, res)
			self.dfs(node.right, res)

# Preorder Iterative
class Solution:
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		res = []
		stack = [root]

		while stack:
			node = stack.pop()
			if node:
				res.append(node.val)
				stack.append(node.right)
				stack.append(node.left)
		return res

# Posorder Recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root,res)
        return res

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            self.dfs(node.right, res)
            res.append(node.val)

# Posorder Iterative
class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		res = []
		stack = [root]

		while stack:
			node = stack.pop()
			if node:
				res.append(node.val)
				stack.append(node.left)
				stack.append(node.right)
		return res[::-1]
