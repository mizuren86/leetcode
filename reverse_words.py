class Solution:
    def reverseWords(self, s: str) -> str:
        # split the words
        # words = ['the', 'sky', 'is', 'blue'], is a list
        words = s.split()

        # reversed words
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)
    
    def rev_rev(self, s: str) -> str:
        words = s.split()
        words = reversed(words)
        return " ".join(words)
    
    def rev_slicing(self, s: str) -> str:
        words = s.split()
        # [start:stop:step]
        return " ".join(words[::-1])

s = 'the sky is blue'
print(Solution().reverseWords(s))