noofrows = int(input())
i = 1 
while i <= noofrows:
    j = 1
    while j <= noofrows-i+1:
        print(j, end = '')
        j = j + 1
    i = i + 1
    print()