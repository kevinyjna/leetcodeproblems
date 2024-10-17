class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num = 0
        length = len(flowerbed)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            
            leftEmpty = (i == 0) or (flowerbed[i-1] == 0)
            rightEmpty = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
            if leftEmpty and rightEmpty:
                num +=1
                flowerbed[i] = 1
                if (num >= n):
                    return True
            
        return num >= n