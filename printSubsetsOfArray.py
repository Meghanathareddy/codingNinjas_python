def printSubsetsHelper(arr,lst):
    n = len(arr)
    if (n == 0):
        for number in lst:
            print(number , end = " ")
        print()
        return
    printSubsetsHelper(arr[1:],lst)
    newLst = lst.copy()
    newLst.append(arr[0])
    printSubsetsHelper(arr[1:],newLst)

def printSubsets(arr):
    printSubsetsHelper(arr,[])


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
output = printSubsets(arr)
