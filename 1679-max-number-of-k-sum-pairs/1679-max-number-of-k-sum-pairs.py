class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        pairs = 0
        for num in nums:
            if d.get(k-num, 0) > 0:
                d[k - num] -= 1
                pairs += 1
            else:
                d[num] = d.get(num, 0) + 1
                
        return pairs