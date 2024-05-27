class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #O(n^2) solution
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
        
        