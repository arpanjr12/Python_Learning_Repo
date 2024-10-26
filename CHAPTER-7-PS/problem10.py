'''
Write a program to print multiplication table of n using for loops in reversed 
order.
'''

num=int(input("enter your number: "))

for i in range(1,11):
    print(f"{num}X{11-i}={num*(11-i)}")
    
