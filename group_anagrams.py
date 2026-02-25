from collections import defaultdict
from typing import List

class Solution:

    # Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            anagrams[key].append(i)
        return list(anagrams.values())

# test cases
ts = Solution()
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
result1 = ts.groupAnagrams(strs1)
print(f"Input: {strs1}, Output: {result1}, Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]")  # Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

strs2 = [""]
result2 = ts.groupAnagrams(strs2)
print(f"Input: {strs2}, Output: {result2}, Expected: [['']]")  # Expected: [['']]   

strs3 = ["a"]
result3 = ts.groupAnagrams(strs3)
print(f"Input: {strs3}, Output: {result3}, Expected: [['a']]")  # Expected: [['a']] 


# d = defaultdict(list)
# d["abc"].append("xyz")
# d["abc"].append("123")
# print(list(d.values()))  # Output: [['xyz', '123']]


