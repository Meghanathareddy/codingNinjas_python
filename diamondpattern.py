noofrows = int(input())
i = 0
odd = 1
while i <= noofrows - 1:

    #spaces
    j = 0
   
    odd =  (2*i) + 1
    while j <= noofrows-(2*i) + 1 :
            print(' ', end = '')
            j = j + 1
    if odd <= noofrows :
       
         #stars
        k = 1
        while k <= ((2*i) + 1):
            print('*',end = '')
            k = k + 1
    
   


    i = i + 1
    print()

'''
spaces = odd -2 
 if odd > noofrows:
        #spaces
        j = 1
        spaces = spaces 
        while j <= noofrows - spaces  :
            print(' ', end = '')
        
'''