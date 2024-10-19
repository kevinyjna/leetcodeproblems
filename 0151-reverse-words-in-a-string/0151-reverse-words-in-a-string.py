class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
                
            start = i
            while i < n and s[i] != ' ':
                i += 1
            end = i
            
            word = s[start:end][::-1]
            result.append(word)
            
        return ' '.join(result)