#checking whether number is prime number or not?
n = int(input())
flag = False
for d in range(2, n ,  1):
    if n % d  == 0:
        flag = True
        break
if flag:
    print("not prime")
else:
    print("prime")

    
