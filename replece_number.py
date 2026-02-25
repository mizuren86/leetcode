class Solution:
    def replaceNumber(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i].isdigit():
                s[i] = 'number'
        return ''.join(s)

test = Solution()
str_1 = 'a1b23c'
result_1 = test.replaceNumber(str_1)
print(f"oringal str is'{str_1}', after replaced str is'{result_1}'. ")
print("-" * 20)