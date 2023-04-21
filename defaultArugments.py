def f1(a,b,c = 2, d = 0):
    return a + b + c + d
print(f1(2,3,4,5)) # 14, c = 4, c= 5
print(f1(2,3)) # 7, c = 2, d = 0
print(f1(2,3,5)) # 10, c = 5, d = 0

f1(b = 2, c = 3, d = 3, a = 10)