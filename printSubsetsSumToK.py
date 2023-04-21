def sum(subsets):
    sum = 0
    for num in subsets:
        sum += num
    return sum

def printSubsetSumToK(nums, k, subsets ,i):
    
    if sum(subsets) == k:
        print(*subsets)
    
    if i == len(nums):
        return
    
    

    subsets.append(nums[i])
    printSubsetSumToK(nums, k, subsets ,i+1)
    
    subsets.pop()
    printSubsetSumToK(nums, k, subsets ,i+1)

n = int(input())
arr = [int(ele) for ele in input().split()]
k = int(input())
printSubsetSumToK(arr, k,[],0)