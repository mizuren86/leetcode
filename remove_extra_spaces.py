class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = ''.join(word[::-1] for word in s.split())
        return s
    
    def reverseWordsTwoPointer(self, s: str) -> str:
        words = s.split()

        left, right = 0, len(words) -1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        return "".join(words)
    
    