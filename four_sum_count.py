from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums: List[int], nums4: List[int]) -> int:
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
        
        # int
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                # n1 + n2 = -(n3 + n4)
                key = -n3-n4
                # n1 + n2 +n3 + n4 =0
                if key in hashmap:
                    count += hashmap[key]
        
        return count
s = Solution()

nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
result1 = s.fourSumCount(nums1, nums2, nums3, nums4)
print(f"test result: {result1} ")