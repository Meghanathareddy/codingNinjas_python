#No multiples of 7
n = int(input())
i = 2
while i <= n:
    if i % 7 == 0:
        i = i + 2
        continue
    print(i)
    i = i + 2
    