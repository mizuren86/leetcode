class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        for i in range(n):
            pro = 1
            for j in range(n):
                if i != j:
                    pro *= nums[j]
            output.append(pro)
        
        return output
                    