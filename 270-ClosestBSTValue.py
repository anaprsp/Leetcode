# Time Complexity O(H)
# Space Complexity O(1)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        closest = 0
        curr = float('inf')

        while root:
            if abs(root.val - target) < curr:
                curr = abs(root.val - target)
                closest = root.val

            if root.val >= target:
                root = root.left

            elif root.val < target:
                root = root.right
        return closest
