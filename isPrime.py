def isPrime(n):
    for d in range(2,n):
        if (n%d == 0):
            break
    else:
        return True
    return False
print(isPrime(5))