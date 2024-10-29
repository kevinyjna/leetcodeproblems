class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 1, 2]
        for i in range (3, n+1):
            ways.append(ways[i-1] + ways[i-2])
        return ways[n]