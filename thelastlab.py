# Cynthia Carter
# CS 125 
# A program that calculates the GCD

import time
def gcdR(x,y):
    if y == 0:
        return x
    else:
        return gcdR(y, x%y)
    

def gcdI(x,y):
    while y != 0:
        temp = y
        y = x%y 
        x = temp
    return x
    
def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    
    looptime = 1000
    timeB = time.time()
    for loop in range(looptime):
        I = gcdI(x,y)
    timeA = time.time()
    print("I = ",I)
    print("elapsed time: ", timeA-timeB)
    
    timeB = time.time()
    for loop in range(looptime):
        R = gcdR(x,y)
    timeA = time.time()
    print("R = ",R)
    print("elapsed time: ", timeA-timeB)

if __name__ == "__main__":
    main()