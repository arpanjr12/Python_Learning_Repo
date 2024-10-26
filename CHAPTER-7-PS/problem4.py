
# Write a program to find whether a given number is prime or not.

n=int(input("enter the number to check: "))

for i in range(2,n):
    if(n%i)==0:
          print(n,"its not a prime number")
          break    
else:
     print(n,"number is a prime number")