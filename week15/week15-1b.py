# week15-1b.py 學習計畫 DP - Multidimention 第1題
# LeetCode 62. Unique Paths 第2種寫法，使用 Bottom-Up DP 建表格
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [ [0] * n for i in range(m) ]  # 建 2D 陣列
        table[0][0] = 1  # 終點1種走法

        for i in range(m):
            for j in range(n):
                if i == 0: table[i][j] = 1
                elif j == 0: table[i][j] = 1
                else: table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]
