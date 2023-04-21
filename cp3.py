
'''
E 
D E 
C D E 
B C D E 
'''
noofrows = int(input())
i =1 
while i <= noofrows:
    j = 1
    start_char = chr(ord('A') + noofrows -i )
    while j <= i:
        charP = chr(ord(start_char) + j -1)
        print(charP, end = ' ')
        j = j + 1
    i = i + 1
    print()