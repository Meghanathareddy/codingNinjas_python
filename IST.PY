'''
i/p:4
o/p:
   1
  121
 12321
1234321
'''

noofrows = int(input())
i = 1 
while i <= noofrows:
    spaces = 1
    #SPACES
    while spaces <= noofrows-i:
        print(' ', end = '')
        spaces = spaces + 1
    p = 1
    j = 1
    #increasing seq
    while j <= i:
        print(j, end = '')
        j = j + 1
        p = p + 1

    #decreasing seq
    p = i -1
    while p >= 1:
        print(p, end = "")
        p = p - 1

    i = i + 1
    print()