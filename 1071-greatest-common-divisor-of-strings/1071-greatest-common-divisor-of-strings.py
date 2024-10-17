class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 > str2:
            longer, shorter = str1, str2
        else:
            shorter, longer = str1, str2
            
        def isDivisible(base, inputStr):
            k = len(inputStr) // len(base)
            if len(inputStr) % len(base) != 0:
                return False
            return base * k == inputStr
        base = shorter
        for i in range(len(base)):
            if isDivisible(base, str1) and isDivisible(base, str2):
                return base
            else:
                base = base[:-1]
                
        return ""
            
        