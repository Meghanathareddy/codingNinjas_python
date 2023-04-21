#getting range of prime number by checking whether number is prime number or not?
n = int(input())
k = 2
while k <= n:
    d = 2
    flag = False
    while d < k:
        if k % d  == 0:
            flag = True
            break
        d = d + 1
    if not flag:
        print(k)
    
    k = k + 1
    

    
