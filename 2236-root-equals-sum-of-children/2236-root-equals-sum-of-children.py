# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        list1=[]
        if not root:
            return 0
        else:
            leftchild=root.left
            rightchild=root.right
            add=leftchild.val+rightchild.val
            if(root.val == add):
                return 1
            else:
                return 0
        
        