class Solution(object):
    def twoSum(self, nums, target):
        diction=dict()
        for index, element in enumerate(nums):
            comp=target-element
            if comp in diction:
                return [index,diction[comp]]
            
            diction[element]=index   # update key and value in dict
        return []
    
            