'''
1
1 2
1 2 3
1 2 3 4
'''
noofrows = int(input())
i =1 
while i <= noofrows:
    j = 1
    while j <= i:
        print(j, end = ' ')
        j = j + 1
    i = i + 1
    print()