noofrows = int(input())
i = 1 
while i <= noofrows:
    spaces = 1
    while spaces <= noofrows-i:
        print(' ', end = '')
        spaces = spaces + 1
    stars = 1
    while stars <= i:
        print('*', end = '')
        stars = stars + 1
    i = i + 1
    print()