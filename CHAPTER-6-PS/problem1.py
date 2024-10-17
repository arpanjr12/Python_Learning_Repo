# Write a program to find the greatest of four numbers entered by the user.

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
d=int(input("enter the fourth number: "))

if(a>b and a>c and a>d):
    print("so the greatest  number is:",a)

elif(b>a and b>c and b>d):
    print("so the greatest  number is:",b)

elif(c>a and c>b and c>d):
    print("so the greatest  number is:",c)

else:
    print("so the greatest  number is:",d)

