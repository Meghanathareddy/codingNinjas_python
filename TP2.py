'''
1
2 3
3 4 5
4 5 6 7
'''
noofrows = int(input())
i =1 
while i <= noofrows:
    j = 1
    p = i
    while j <= i:
        print(p, end = ' ')
        j = j + 1
        p = p + 1
    i = i + 1
    print()