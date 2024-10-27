#  Write a recursive function to calculate the sum of first n natural numbers

#  so the formula is sum of n => sum(n-1)+n


def sun(n):
    
    if(n==1):
        return 1
    else:
     return sun(n-1)+n
n=int(input("enter the number: "))
print(sun(n))