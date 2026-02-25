class Solution:
    def conConstruct1(self, ransomNote: str, magazine:str) -> bool:
        r_list = list(ransomNote)
        for char_m in magazine:
            for j in range(len(r_list)):
                if char_m == r_list[j]:
                    r_list.pop(j)
                    break
        
        if len(r_list) == 0:
            return True
        return False
    def conConstruc2(self, ransomNote: str, magazine:str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))
        

s = Solution()
ransomNote_1 = "aa"
magazine_1 = "aab"
result1 = s.conConstruct1(ransomNote_1, magazine_1)
print(f"{result1}")