'''Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. 
 Assume 3 subjects and take marks as an input from the user.'''


m1=int(input("enter marks one: "))
m2=int(input("enter marks two: "))
m3=int(input("enter marks three: "))

total_parcentage=(m1+m2+m3)/3

if(total_parcentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("result passed: , and the parcentage is:",total_parcentage )

else:
    print("result fail and the parcentage is:",total_parcentage)

