# week09-3.py 學習計畫 Linked List 第3題 Easy 題 (使用「函式呼叫函式」Recursion)
# week09-2.py 學習計畫 Linked List 第3題 Easy 題 (先變陣列、再變成 Linked List)
# LeetCode 206. Reverse Linked List
# 把它反過來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # week09-3.py
        if head == None or head.next == None: return head  # 終止條件（最簡單的狀況）

        head2 = head.next
        ans = self.reverseList(head.next)  # 函式呼叫函式 (遞迴)

        head2.next = head
        head.next = None

        return ans
