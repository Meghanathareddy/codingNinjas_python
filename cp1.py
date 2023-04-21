'''
A B C D
A B C D
A B C D
A B C D
'''
noofrows = int(input())
i =1 
while i <= noofrows:
    j = 1
    while j <= noofrows:
        charP = chr(ord('A') + j - 1)
        print(charP, end = ' ')
        j = j + 1
    i = i + 1
    print()