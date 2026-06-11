# week16-4.py 學習計畫 Intervals 第2題 2026-06-11
# LeetCode 452. Minimum Number of Arrows to Burst Balloons
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort( key = lambda x:x[1] ) # 氣球照「右邊界」排序
        ans = 0

        previous_end = -float('inf')
        for start, end in points: # 逐一取出氣球
            if previous_end < start: # 氣球有距離哦！只好再多射1箭
                ans += 1 # 要為現在的 [start, end] 的氣球，射1箭
                previous_end = end

        return ans
