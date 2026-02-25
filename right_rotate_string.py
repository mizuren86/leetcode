class Solution:
    def rightRotateString(self, s: str, k: int) -> str:
        # Get the length of the string
        n = len(s)

        # make sure k effective
        k = k % n

        # string[start:end]
        # 1. s[n-k:]: Takes the last k characters
        # 2. s[:n-k]: Takes the first(n-k) characters
        s = s[n-k:] + s[:n-k]
        return s
    
s = 'abcdefg'
k = 2
print(Solution().rightRotateString(s,k))