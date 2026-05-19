from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1          # empty path base case

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            count = prefix[curr_sum - targetSum]

            prefix[curr_sum] += 1          # add current path to map

            count += dfs(node.left,  curr_sum)
            count += dfs(node.right, curr_sum)

            prefix[curr_sum] -= 1          # ← CRITICAL: backtrack!
            return count

        return dfs(root, 0)