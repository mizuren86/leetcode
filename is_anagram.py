class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # int[] , array
        record = [0] * 26

        for i in s:
            # record ACSII in string s, and +1
            record[ord(i) - ord("a")] += 1
        for i in t:
            # record ACII in string t, and -1
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True