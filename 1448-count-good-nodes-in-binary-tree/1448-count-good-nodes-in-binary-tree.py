class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]   # (node, max_so_far)
        count = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
            new_max = max(max_val, node.val)
            if node.left:  stack.append((node.left,  new_max))
            if node.right: stack.append((node.right, new_max))

        return count