def isPrime(n):
    for d in range(2,n):
        if (n%d == 0):
            break
    else:
        return True
    return False

def primeFrom2toN(n):
    for k in range(2, n + 1):
        #check k is prime and in case it is prime we print k
        is_k_prime = isPrime(k)
        if is_k_prime:
            print(k)

primeFrom2toN(20)