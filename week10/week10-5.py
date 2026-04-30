# week10-5.py 學習計畫 Binary Tree - DFS 第4題
# LeetCode 437. Path Sum III
# 從上到下，有沒有一小段「加起來是 targetSum」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1 # 有 1 個上帝視角的 0
        def helper(root, total): # 之前的 total
            if root == None: return 0
            total += root.val
            # 先看之前有沒有出現過 (total - targetSum) 的路徑
            ans = counter[total - targetSum]

            counter[total] += 1 # 累積多 1 個 total (的斷點)
            ans += helper(root.left, total)
            ans += helper(root.right, total)
            counter[total] -= 1 # 再扣掉 (Backtracking 回溯)

            return ans
        return helper(root, 0)
