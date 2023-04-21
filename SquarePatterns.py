#/*
#4 3 2 1
#4 3 2 1
#4 3 2 1
#4 3 2 1
#*/

noofrows = int(input())
i =1 
while i <= noofrows:
    j = 1
    while j <= noofrows:
        print(noofrows - j + 1, end = ' ')
        j = j + 1
    i = i + 1
    print()
    