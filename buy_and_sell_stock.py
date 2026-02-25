class solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        #         return max_profit
        # return max_profit
        min_price = float('inf')

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price 

        return max_profit

#test cases
ts = solution()
prices1 = [7, 1, 5, 3, 6, 4]
result1 = ts.maxProfit(prices1)
print(f"Input: {prices1}, Output: {result1}, Expected: 5")  # Expected: 5

prices2 = [7, 6, 4, 3, 1]
result2 = ts.maxProfit(prices2)
print(f"Input: {prices2}, Output: {result2}, Expected: 0")  # Expected: 0
