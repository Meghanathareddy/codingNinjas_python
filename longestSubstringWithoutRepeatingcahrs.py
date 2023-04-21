class Solution:
    def lengthOflongestSubstring(self, s:str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end +1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True
        
        
        n = len(s)
        res = 0 
        for i in range(n):
            for j in range(n):
                if check(i, j):
                    res = max(res, j -i +1)
                else:
                    break
            print(i, j,res)
        return res

s = Solution()
print(s.lengthOflongestSubstring(input()))       