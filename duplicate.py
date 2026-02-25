import collections

class sol:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    
# test cases

testsol = sol()

nums1 = [1, 2, 3, 3]
result1 = testsol.hasDuplicate(nums1)
print(f"Input: {nums1}, Output: {result1}, Expected: True ")  # Expected: True

nums2 = [1, 2, 3, 4]
result2 = testsol.hasDuplicate(nums2)
print(f"Input: {nums2}, Output: {result2}, Expected: False")


