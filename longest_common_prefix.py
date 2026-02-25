class Solution:
    def longestCommonPrefix(self, strs):
        # edge case
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            while not s.startswith(prefix):
                # Reduce the prefix by one character from the end
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# test cases
ts = Solution()
strs1 = ["flower", "flow", "flight"]
result1 = ts.longestCommonPrefix(strs1)
print(f"Input: {strs1}, Output: '{result1}', Expected: 'fl'")  # Expected: 'fl'

strs2 = ["dog", "racecar", "car"]
result2 = ts.longestCommonPrefix(strs2)
print(f"Input: {strs2}, Output: '{result2}', Expected: ''")  # Expected: ''

nums3 = [1]
result3 = ts.longestCommonPrefix(nums3)
print(f"Input: {nums3}, Output: '{result3}', Expected: '1'")  # Expected: '1'