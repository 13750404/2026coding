# week15-2a.py 學習計畫 DP - Multidimention 第2題
# LeetCode 1143. Longest Common Subsequence 第1種寫法 Top-Down 函式呼叫函式
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)  # 兩字串的長度
        @cache  # 函式呼叫函式
        def helper(i, j):
            if i == M or j == N: return 0
            if text1[i] == text2[j]: return 1 + helper(i+1, j+1)  # 下一位
            else: return max( helper(i, j+1), helper(i+1, j) )
            # 不相同，就跳過上面 or 跳過下面，看誰比較長，就 return 誰
        return helper(0, 0)  # 函式呼叫函式
