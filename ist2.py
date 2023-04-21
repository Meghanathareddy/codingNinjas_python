noofrows = int(input())
i = 1 
while i <= noofrows:
    spaces = 1
    #SPACES
    while spaces <= noofrows-i:
        print(' ', end = '')
        spaces = spaces + 1
   
    j = i
    #decreasing seq
    while j >= 1:
        print(j, end = '')
        j = j - 1
    #increasing seq
    p = 2
    while p >= i:
        print(p, end = "")
        p = p - 1
    i = i + 1
    print()