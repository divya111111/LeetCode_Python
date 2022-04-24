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
                return 0
            
            if (root.val < low):    #then  only right traversal needed
                sumbst(root.right)
            
            elif (root.val > high):   # then only left traversal needed
                sumbst(root.left)
            else:
                self.sum1+=root.val
                sumbst(root.left)
                sumbst(root.right)
        sumbst(root)
        return self.sum1
        