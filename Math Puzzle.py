'''
Jackson Duchow
Sdev220
This program finds any number that can be multpied by 4 and be reversed ie:2178*4=8721

The time it takes the CPU to search through depends on how many digits the user inputs.
The more digits, the bigger the range of numbers to search through.
By reducing the range of numbers, the amount of time is also reduced.
Adding ways to sort the numbers more increase the time effeciency of the current code
due to added calculations Python must do, such as taking the first two digits reversed and chcecking to 
see if it is divisible by 4.

For wether or not time is an issue, the answer depends on how many digits and hardware.
Modern CPUS are fast, allowing for each calculation to be miniscule in time, but with a range
that grows exponentialy with the num,ber of digits, the time grows with it.
'''

import time

def reverseVerifier(x):
    #turns x into a string and reverses it
    rev = str(x)[::-1]
    #string of the product of x and 4
    prod = str(x*4)
    #returns the string comparison of the product and the reversed string
    return str(prod) == rev

#finds any number with specified number of digits
def reverseFinder(digits):
    #range is detemined by taking every number with specified digits
    # and dividing by 4: 
    # 10^d-1<x*4<10^d
    # 10^d-1/4<x<10^d/4   
    # this make the lower bound have less than specified digts, so instead of dividing loewr bound by 4
    # I multiply it by since the first number can never be 1 since that would make the reverse an odd number
    #also only allows even numbers since a number multiplied by 4 becomes even, even if it is an odd number, odd*4=even
    for i in range(10**(digits-1)*2,10**(digits)//4,2):
        if reverseVerifier(i):
            #prints any number that passes reverseVerifier
            print(i)


if __name__ == "__main__":
    #gets the number of digits
    digits = int(input("Enter the number of digits: "))
    #starts a timer
    start_time = time.time()
    reverseFinder(digits)
    #ends the timer
    end_time = time.time()
    #prints the runtime by subtracting end time from start time
    print(f"Runtime: {end_time - start_time} seconds")
