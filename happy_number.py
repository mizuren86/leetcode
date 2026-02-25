class Solution:
    def get_next(self, n:int) -> int:
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit * digit
            n //= 10
        return total_sum
    def isHappy(self, n:int) -> bool:
        seen_numbers = set()
        current = n

        while current != 1:
            if current in seen_numbers:
                return False
            seen_numbers.add(current)
            current = self.get_next(current)
        
        return True
    
s = Solution()

n1 = 19
result1 = s.isHappy(n1)
print(f"input n = {n1}")
print(f"expect result: True, actually: {result1}")
print("-" * 20)

n2 = 2
result2 = s.isHappy(n2)
print(f"input n = {n2}")
print(f"expect result: False, actually: {result2} ")
