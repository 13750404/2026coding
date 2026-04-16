#week08-2.py 學習計畫Binary Search 第1題
# 給你 guess() 你可以呼叫它，找出 1...n 裡面的「答案」

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#         1 if num is lower than the picked number
#         otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # for i in range(1, n+1) # 其實是的暴力法，你把區間找答案
        #     if guess(i) == 0: return i  # 猜中了，答案是 i

        # 不使用上面的 for 迴圈，因為 n 有 2^31 那麼大，試不完
        # 要用小圈「猜數字」每次縮小範圍，一半一半，比大小，縮小範圍
        left, right = 1, n + 1  # 左右的範圍（左：包含，右：不包含）

        while left < right:  # 左右的範圍沒有「擠在一起」
            mid = (left + right) // 2  # 中間的數（請寫 mid）

            if guess(mid) == 0:
                return mid  # 猜中間的數字
            if guess(mid) > 0:
                left = mid + 1  # 暗示你，往右一點（中點設成下界）
            else:
                right = mid  # 暗示你，再往左（中點設成上界）

        return left
