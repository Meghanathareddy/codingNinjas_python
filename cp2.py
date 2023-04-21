'''
A B C D
B C D E
C D E F
D E F G
'''
noofrows = int(input())
i =1 
while i <= noofrows:
    j = 1
    start_char = chr(ord('A') + i- 1)
    while j <= noofrows:
        charP = chr(ord(start_char) + j - 1)
        print(charP, end = ' ')
        j = j + 1
    i = i + 1
    print()