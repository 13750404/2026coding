# week16-1.py 學習計畫 Backtracking 第1題 2026-06-11
# LeetCode 17. Letter Combinations of a Phone Number
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        table = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def helper(i, prefix):
            # 處理第 i 個字母，prefix 前面累積字母
            if i == len(digits): # 長度湊齊 N 個，完整了
                ans.append(prefix) # 塞入答案
                return # 結束

            for c in table[ int( digits[i] ) ]:
                helper(i + 1, prefix + c)

        helper(0, "")
        return ans
