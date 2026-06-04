# week15-2b.py 學習計畫 DP - Multidimention 第2題
# LeetCode 1143. Longest Common Subsequence 第2種寫法 Bottom-Up 建表格
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)  # 兩字串的長度
        table = [ [0] *(N+1) for i in range(M+1) ]
        for i in range(M):
            for j in range(N):
                #case1 = table[i-1][j] 看上面
                #case2 = table[i][j-1] 看左邊
                #case3 = table[i-1][j-1] + 1 看左上角 (如果相同時, 看左上角 + 1)
                if text1[i] == text2[j]: table[i+1][j+1] = table[i][j] + 1
                table[i+1][j+1] = max(table[i+1][j+1], table[i][j+1], table[i+1][j])
        return table[M][N]
