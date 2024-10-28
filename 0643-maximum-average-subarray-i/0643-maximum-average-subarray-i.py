class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        
        max_avg = 0
        sliding_num = 0
        for i in range(k):
            sliding_num += nums[i] 
            max_avg = sliding_num / k
            
        while right < len(nums) - 1:
            right += 1
            sliding_num = sliding_num - nums[left] + nums[right]
            left += 1
            max_avg = max(max_avg, (sliding_num)/k)
        return max_avg
