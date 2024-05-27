class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # #Nested loop: Time complexity O(n^2) solution
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] < target:
        #             count += 1
        # return count
        
        #Two pointer: Time complexity O(n*log n)
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count
        