# week15-4b.py 學習計畫 DP - Multidimension 第4題
# LeetCode Editing Distance 編輯(插入1字母、刪除1字母、換掉1字母)幾次後，會得到 word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2) # 兩字串的長度
        a = [[0] * (N + 1) for i in range(M + 1)]
        for i in range(M + 1): a[i][0] = i
        for j in range(N + 1): a[0][j] = j
        for i in range(M):
            for j in range(N):
                a[i+1][j+1] = min(a[i][j+1], a[i+1][j], a[i][j]) + 1
                if word1[i] == word2[j]: a[i+1][j+1] = a[i][j]
        return a[M][N]
