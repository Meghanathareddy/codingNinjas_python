from doctest import OutputChecker


def subsets(arr):
    n = len(arr)
    if(n <= 0):
        output = [[]]
        return output
    output = subsets(arr[:n-1])
    outputLen = len(output)

    for i in range(0, outputLen):
        output.append(output[i].copy())
        output[outputLen+i].append(arr[n-1])
    return output

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
output = subsets(arr)
for lst in output:
    for num in lst:
        print(num, end = " ")
    print()