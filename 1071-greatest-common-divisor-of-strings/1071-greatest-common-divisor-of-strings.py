class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        
        if len(str1) < len(str2):
            shorter, longer = str1, str2
        else:
            shorter, longer = str2, str1
        
        def isDivisible(baseStr, inputStr):
            if (len(inputStr) % len(baseStr) != 0) :
                return False
            repeatCount = len(inputStr) // len(baseStr)
            return repeatCount * baseStr == inputStr

        base = shorter
        while (len(base) > 0) :
            if isDivisible(base, shorter) and isDivisible(base, longer):
                return base
            else:
                base = base[:-1]
        
         
        return ""
        
                