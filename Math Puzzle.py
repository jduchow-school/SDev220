'''
Jackson Duchow
Sdev220
This program finds any number that can be multpied by 4 and be reversed ie:2178*4=8721


'''



def reverseVerifier(x):
    #turns x into a string and reverses it
    rev = str(x)[::-1]
    #string of the product of x and 4
    prod = str(x*4)
    #returns the string comparison of the product and the reversed string
    return str(prod) == rev

def reverseFinder(digits):    
    for i in range(10**(digits-1),10**(digits)):
        if reverseVerifier(i):
            print(i)

reverseFinder(10)