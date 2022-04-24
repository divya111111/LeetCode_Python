# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum1=0
        def sumbst(root):
           
            if not root:
                return []
            else:
                return sumbst(root.left)+[root.val]+sumbst(root.right)
        l1=sumbst(root)
        print(l1)
        k=0
        for i in l1:
            if((i>low) and (i<high)):
                   k=k+i
        sum1=k+low+high
        #print(sum1)
        return sum1
        