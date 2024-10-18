class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        vowel_set = set("aeiouAEIOU")
        list(s)
        while(left < right):
            if s[left] not in vowel_set:
                left += 1
            elif s[right] not in vowel_set:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
       
        return ''.join(s)
                