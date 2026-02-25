from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # heap法
        # # 1. 統計頻率
        # freq_map = Counter(nums)
        # # example: Counter({3: 3, 2: 2, 1: 1})
        # print(f"Frequency Map: {freq_map}")

        # # 2. 字串處理
        # # 根據頻率降序排序，並取出鍵 (key)
        # # items() 會返回 (key, value) 元組
        # # lambda x: x[1] 表示以元組的第二個元素 (頻率) 排序
        # sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        # # 3. 取出前 k 個元素的數字
        # result = [item[0] for item in sorted_items[:k]]
        
        # bucket法
        # 步驟 1: 計算頻率
        counts = Counter(nums)
        
        # 步驟 2 & 3: 創建桶並將數字放入
        # 桶數組的索引代表頻率，值是具有該頻率的數字列表
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
            
        # 步驟 4: 收集結果
        result = []
        # 從最高頻率開始遍歷桶
        for i in range(len(buckets) - 1, 0, -1):
            # 將當前桶中的所有數字添加到結果列表
            for num in buckets[i]:
                result.append(num)
                # 如果結果列表大小達到 k，則返回
                if len(result) == k:
                    return result
            
        # return result

# test cases
ts = Solution()
nums = [1, 2, 2, 3, 3, 3]
k = 2
print(f"Input: nums = {nums}, k = {k}, Output: {ts.topKFrequent(nums, k)}") # Output: [3, 2] 或 [2, 3]

nums2 = [1, 1, 1, 2, 2, 3]
k2 = 2
print(f"Input: nums = {nums2}, k = {k2}, Output: {ts.topKFrequent(nums2, k2)}") # Output: [1, 2]

nums3 = [1]
k3 = 1
print(f"Input: nums = {nums3}, k = {k3}, Output: {ts.topKFrequent(nums3, k3)}") # Output: [1]

nums4 = [1, 2, 3, 4, 5]
k4 = 3
print(f"Input: nums = {nums4}, k = {k4}, Output: {ts.topKFrequent(nums4, k4)}") # Output: [1, 2, 3] 或其他組合


