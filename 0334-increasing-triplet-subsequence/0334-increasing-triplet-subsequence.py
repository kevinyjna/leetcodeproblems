class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        num_i = num_j = float('inf')
        
        for num in nums:
            if num_i >= num:
                num_i = num
            elif num_j >= num:
                num_j = num
            else:
                return True
        return False