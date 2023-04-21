#No multiples of 7 with For loop
n = int(input())
i = 2
for i in range(2, n + 1, 2):
    if i % 7 == 0:
        continue
    print(i)