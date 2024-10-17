#  Write a program to accept marks of  of 6 students and display them in a sorted manner.
marks=[]
f1=int(input("enter marks of student 1: "))
marks.append(f1)

f2=int(input("enter marks of student 2: "))
marks.append(f2)

f3=int(input("enter marks of student 3: "))
marks.append(f3)

f4=int(input("enter marks of student 4: "))
marks.append(f4)

f5=int(input("enter marks of student 5: "))
marks.append(f5)

f6=int(input("enter marks of student 6: "))
marks.append(f6)

marks.sort()
print(marks)
