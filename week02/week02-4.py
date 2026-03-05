# week02-4.py 學習計畫 Two Pointers 第3題 Medium 題
# LeetCode 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0  # 一開始沒有答案
        i, j = 0, len(height) - 1  # 左邊 i 右邊 j
        while i < j:  # 只要左右還沒撞在一起
            # 算出現在的面積：底 (j-i) * 高 (取矮的那一邊)
            area = (j - i) * min(height[i], height[j])
            ans = max(ans, area)  # 更新答案
            if height[i] < height[j]:
                i += 1  # 小的 i，往右
            else:
                j -= 1  # 小的 j，往左
        return ans
