class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                # print(i)
                # print(j)
                sum1=nums[i]+nums[j]
                if(sum1 == target):
                    list1.append(i)
                    list1.append(j)
                
        return list1
            
        