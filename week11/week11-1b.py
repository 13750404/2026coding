# week11-1b.py 學習計畫 Binary Tree - DFS 第2題 Easy題
# LeetCode 872. Leaf-Similar Trees
# 想知道 binary tree 裡的 leaf 組出來，是否都相同
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a, b = [], []
        def helper(root, a):
            if root.left == None and root.right == None:  # 葉子
                a.append( root.val ) # 把值加入 a
            if root.left:  helper(root.left, a)  # 如果左邊有
            if root.right: helper(root.right, a) # 如果右邊有
        helper(root1, a)
        helper(root2, b)
        return a == b
