class Solution:
    def palindrome(self, x: int) -> bool:
        rev = 0
        
        if (x < 0 )  :
            return False
        orig = x
        while x != 0 :
            rev = rev * 10 + x % 10
            x = x // 10

        return orig == rev

s = Solution()
print(s.palindrome(int(input())))

