'''Write a Python Program for n-th Fibonacci number.
Fn = Fn-1 + Fn-2

with seed values

F0 = 0 and F1 = 1.'''



def Fibonacci():
    n=int(input('enter num of which you want Fibonacci number: '))
    if n<0: 
        print("Incorrect input") 
# First Fibonacci number is 0 
    elif n==1: 
     return 0
# Second Fibonacci number is 1 
    elif n==2: 
     return 1
    else: 
     return (n-1)+r(n-2)
print(Fibonacci())
