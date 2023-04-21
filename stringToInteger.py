from ast import Pow
from ctypes.wintypes import INT
from unicodedata import digit
from unittest import result


class Solution:
    def myAtoi(self, input:str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(input)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = - pow(2, 31)

        #Discard all spaces from the beginning of the input String.
        while index < n and input[index] == ' ':
            index += 1
        
        #sign = +1, if it's Positive number, otherwise sign = -1
        if index < n and input[index] == '+':
            index += 1
            sign  = 1
        elif index < n and input[index] == '-':
            index += 1
            sign  = -1
        
        #Traverse next digits of input and stop if it is not a digit.

        #End of String is also non-digit character.
        while index < n and input[index].isdigit():
            digit = int(input[index])

            #check overflow and underflow conditions
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):

                # if integer overflowed and return 2^31 - 1 , otherwise if underflowed return - 2^ 31
                return INT_MAX if sign == 1 else INT_MIN

                #Append current Digit to the result.
            result = 10* result + digit
            index += 1

            # we have formed a valid number without any overflow/underflow
            #Return it after multiplying it with its sign.
        return sign * result
                  
s = Solution()
print(s.myAtoi("  -457 -word 14"))


"""
Complexity Analysis

If N is the number of characters in the input string.

Time complexity: O(N)

We visit each character in the input at most once and for each character we spend a constant amount of time.

Space complexity: O(1)

We have used only constant space to store the sign and the result.
"""
