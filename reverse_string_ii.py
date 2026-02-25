class Solution:
    def reverseStringII(self, s: str, k: int) -> str:
        # for python can't doing string only 
        s = list(s)
        n = len(s)
        for i in range(0, n, 2 * k):
            end = min (i + k - 1, n - 1)
            left, right = i, end
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            if i+k <= len(s):
                s[i:i+k] = reversed(s[i:i+k])
            else:
                s[i:len(s)] = reversed(s[i:len(s)])
        return ''.join(s)
        
       
s = 'abcdefg'
k = 2
print(Solution().reverseStr(s,k))