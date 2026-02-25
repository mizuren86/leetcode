class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float("inf") else 0

# test cases
testsol = Solution()
target1 = 7
nums1 = [2, 3, 1, 2, 4, 3]
result1 = testsol.minSubArrayLen(target1, nums1)
print(f"Input: target = {target1}, nums = {nums1}, Output: {result1}, Expected: 2")  # Expected: 2

