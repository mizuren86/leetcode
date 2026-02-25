class Solution:
    def singleNumber(self, nums:list[int]) -> int:
        # hashset = set()
        # for i in nums:
        #     if i in hashset:
        #         hashset.remove(i)
        #     else:
        #         hashset.add(i)
        # return hashset.pop()
        result = 0 
        for i in nums:
            result ^= i
        return result


# test cases
ts = Solution()
nums1 = [2, 2, 1]
result1 = ts.singleNumber(nums1)
print(f"Input: {nums1}, Output: {result1}, Expecterd: 1")  # Expected: 1

nums2 = [4, 1, 2, 1, 2]
result2 = ts.singleNumber(nums2)
print(f"Input: {nums2}, Output: {result2}, Expected: 4")  # Expected: 4

