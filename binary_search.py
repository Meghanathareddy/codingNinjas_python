from typing import List


class Solution:
    def search(self, nums:List[int], target:int) -> int:
        #set the left and right boundaries
        left = 0
        right = len(nums) - 1

        #under this condition
        while left <= right:

            #Get the middle index and the middle value.
            mid = (left + right) // 2
            #case1: return the middle index.
            if nums[mid] == target:
                return mid
            #case2: discard the smaller half
            elif nums[mid] < target:
                left = mid + 1

             #case3: discard the larger half
            else:
                right = mid -  1
            
        #If we finish the search without , return -1
        return -1

s = Solution()
n = int(input())
arr = [0]* n
for i in arr:
    arr[i] = int(input())
target = int(input())
print(s.search(arr, target))
