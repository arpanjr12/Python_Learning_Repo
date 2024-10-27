
# Recursion is a function which calls itself. It is used to directly use a mathematical formula as function.

'''
factorial(0)=1
factorial(1)=1
factorial(2)=2 X 1
factorial(3)=3 x 2 x 1
factorial(4)=4 x 3 x 2 x 1
factorial(5)=5 x 4 x 3 x 2 x 1
factorial(n)=n x(n-1) x.....x 3 x 2 x 1

factorial(n)=n * factorial(n-1)
'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
n=int(input("enter the  number: "))
print(f"the factorial of given number is: {factorial(n)}")


