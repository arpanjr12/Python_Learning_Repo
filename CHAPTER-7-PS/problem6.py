
#Write a program to calculate the factorial of a given number using for loop.

n=int(input("enter the number: "))

fact=1
for i in range(1,n+1):
    fact=fact * i

print(f"the factorial of {n} is",fact)

