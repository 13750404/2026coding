# week09-6.py 學習計畫 Linked list 第2題
# LeetCode 328. Odd Even Linked List 偶數堆、奇數堆,串起來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = [] # 這題竟然可以用作弊法，先轉成陣列 a
        while head: # 逐一將 Linked List 的值，放入陣列 a
            a.append( head.val )
            head = head.next # 記得要換下一筆哦！

        N = len(a) # 陣列的大小
        now = ans = ListNode() # 答案,有個 Node 右邊會塞真的 Nodes
        for i in range(0, N, 2): # 索引為偶數的堆 (第1, 3, 5...個節點)
            now.next = ListNode( a[i] ) # 逐一塞進去
            now = now.next # 串接下一個

        for i in range(1, N, 2): # 索引為奇數的堆 (第2, 4, 6...個節點)
            now.next = ListNode( a[i] ) # 逐一塞進去
            now = now.next # 串接下一個

        return ans.next
