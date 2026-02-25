class solutin:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
# test cases
ts = solutin()
s1 = "Was it a car or a cat I saw?"
print(f"Input: s = '{s1}', Output: {ts.validPalindrome(s1)}")  # Output: True

s2 = "Hello, World!"
print(f"Input: s = '{s2}', Output: {ts.validPalindrome(s2)}")  # Output: False