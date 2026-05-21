# week13-3.py 學習計畫 Heap / Priority Queue 第1題
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 先用作弊的寫法示範一次
        #nums.sort(reverse=True) # 先大到小排好
        #return nums[k-1] # 第k大的數，是 0...k-1

        # 要用 Heap 資料結構，可以找出最小的數
        #heapify(nums) # 變成 heap 資料結構
        #while nums:
        #    print( heappop(nums) )

        # 最後用這個版本
        heapify(nums) # 變成 heap 資料結構
        for i in range(len(nums)-k):
            heappop(nums) # 吐掉不用的
        return heappop(nums) # 剩下的那個,就是第k大的。
