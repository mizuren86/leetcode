from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute force approach
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # using a hash map to store the indices of the numbers
        hashset = {}

        for i, num in enumerate(nums):
            # create the variable complement which is the difference between target and the current number
            complement = target - num
            if complement in hashset:
                # if the complement exists in the hashset, return the indices
                return [hashset[complement], i] 
            
            # otherwise, store the current number and its index in the hashset
            hashset[num] = i
        return "no twosum target exist"

# test cases
ts = Solution()
nums1 = [2, 7, 11, 15]
result1 = ts.twoSum(nums1, 9)
print(f"Input: {nums1}, Target: 9, Output: {result1}, Expected: [0, 1]")  # Expected: [0, 1]    

nums2 = [3, 2, 4]
result2 = ts.twoSum(nums2, 6)
print(f"Input: {nums2}, Target: 6, Output: {result2}, Expected: [1, 2]")  # Expected: [1, 2]   

nums3 = [6,9,0,6]
result3 = ts.twoSum(nums3, 16)
print(f"Input: {nums3}, Target: 16, Output: {result3}, Expected: no twosum target exit") # Expected: no twosum target exit
