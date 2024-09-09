class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        i = 0
        while i < len(nums):
            temp = target - nums[i]
            if temp in hash:
                return [i, hash[temp]]
            hash[nums[i]] = i
            i+=1
            