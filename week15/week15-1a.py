# week15-1a.py 學習計畫 DP - Multidimention 第1題
# LeetCode 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(i, j):  # 函式呼叫函式，現在若在 (i,j)座標
            if i == m-1 and j == n-1: return 1  # 走到終點，成功
            if i == m or j == n: return 0  # 走超過邊界，失敗
            return helper(i+1, j) + helper(i, j+1)  # 函式呼叫函式
        return helper(0, 0)  # 函式呼叫函式
