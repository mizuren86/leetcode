class Solution:

    def encode(self, strs: list[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            # 找出長度（直到遇到 #）
            # int j
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # j 是 #，j+1 是字串起點，長度為 length
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
    
# test cases
ts = Solution()
list1 = ["lint", "code", "love", "you"]
encoded1 = ts.encode(list1)
print(encoded1)  # Output: "4#lint4#code4#love3#you"
decoded1 = ts.decode(encoded1)
print(decoded1)  # Output: ["lint", "code", "love", "you"] 