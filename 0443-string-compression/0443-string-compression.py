class Solution:
    def compress(self, chars: List[str]) -> int:
# pointer for writing compressed characters
        index = 0 
# pointer for traversing chars list
        i = 0
        while i < len(chars):
            currChar = chars[i]
            count = 1
            while i + 1 < len(chars) and chars[i+1] == currChar:
                i+=1
                count += 1
                
            chars[index] = currChar
            index+=1
            if count > 1:
                countStr = str(count)
                for c in countStr:
                    chars[index] = c
                    index += 1
                    
            i+=1
        return index
            
                