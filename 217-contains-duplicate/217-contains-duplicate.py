class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset=set()
        for x in nums:
            if x not in hashset:
                hashset.add(x)
            else:
                return True
        return False