import sys
from unicodedata import digit
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while(x != 0):
            pop = x % 10 # last digit
            x = x//10 # remainging digit
            if (rev > sys.maxsize//10 or (rev == sys.maxsize//10 and pop > 7)):
                return 0
            if (rev < (-sys.maxsize - 1)//10 or (rev == (-sys.maxsize - 1)//10 and pop < -8 )):
                return 0
            rev = rev * 10 + pop
        
        return rev

s = Solution()
print(s.reverse(-13))


