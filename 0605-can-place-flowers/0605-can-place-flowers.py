class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num = 0
        for i in range(len(flowerbed)):
            left = True if i == 0 or flowerbed[i-1] == 0 else False
            right = True if i == len(flowerbed) - 1 or flowerbed[i+1] == 0 else False
            if (left and right and flowerbed[i] != 1):
                num +=1
                flowerbed[i] = 1
            
        return True if num >= n else False