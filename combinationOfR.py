'''
combination of n,r = ncr
'''
def fact(n):
    n_fact = 1
    for i in range(1, n + 1):
        n_fact = n_fact * i
    return n_fact

def ncr(n, r):
    
    n_fact = fact(n)
    r_fact = fact(r)
    n_r_fact = fact(n-r)
    ans = n_fact//(r_fact*n_r_fact)
    return ans 

n = int(input())
r = int(input())
print(ncr(n, r))