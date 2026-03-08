'''
Jackson Duchow
Sdev220
This program finds any number that can be multpied by 4 and be reversed ie:2178*4=8721


'''



def reverseFinder(x):
    
    rev = str(x)[::-1]
    prod = x*4
    if str(prod) == rev:
        return True
    else: 
        return False
    
print(reverseFinder(2171))