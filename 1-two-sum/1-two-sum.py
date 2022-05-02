class Solution(object):
    def twoSum(self, nums, target):
        diction=dict()
        for index, value in enumerate(nums):
            comp=target-value
            if comp in diction:
                return [ diction[comp], index]
            else:
                diction[value]=index
        return []
                
                

    
            