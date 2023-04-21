import sys
def minCost(cost, i, j, n, m):
    
    #special case:
    if i ==n-1 and j ==m-1:
        return cost[i][j]

    #Base case
    if i >= n or j >= m:
        return sys.maxsize
    

    ans1  = minCost(cost, i, j+1, n, m)
    ans2 = minCost(cost, i+1, j, n,m)
    ans3 = minCost(cost, i+1, j+1, n, m)

    ans = cost[i][j] + min(ans1, ans2, ans3)
    return ans


cost = [[1,5,11],[8, 13,12],[2, 3,7]]
n = 4
m = 3
ans = minCost(cost, 0, 0, 4, 3)
print(ans)