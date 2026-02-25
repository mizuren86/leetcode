class Solution:
    def commonChars(self, words: List[str]) -> list[str]:
        if not words: return []
        result = []
        # 用来统计所有字符串里字符出现的最小频率
        hash = [0] * 26
        # 用第一个字符串给hash初始化
        for i, c in enumerate(words[0]):
            hash[ord(c) - ord('a')] += 1
        # 统计除第一个字符串外字符的出现频率
        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for j in range(len(words[i])):
                c = words[i][j]
                hashOtherStr[ord(c) - ord('a')] += 1
            # 更新hash，保证hash里统计26个字符在所有字符串里出现的最小次数
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])
        for i in range(26):
            while hash[i] != 0:
                # convert ACII to words
                chr_to_add = chr(i + ord('a'))
                result.append(chr_to_add)
                hash[i] -= 1
        return result