class Solution:
    # two pointers
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
       
        left, right = 0, len(s)-1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    # stack
    def reverseString1(self, s: list[str]) -> None:
        stack = []
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i] = stack.pop()

    # reverse()
    def reverseString(self, s: list[str]) -> None:
        s.reverse()



s1 = ["h", "e", "l", "l", "o"]
sol = Solution()
sol.reverseString(s1)
print(s1)

