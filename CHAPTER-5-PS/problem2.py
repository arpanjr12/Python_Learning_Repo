#Write a program to input eight numbers from the user and display all the unique numbers (once)

s=set()

num=int(input("enter number 1: "))
s.add(num)

num=int(input("enter number 2: "))
s.add(num)

num=int(input("enter number 3: "))
s.add(num)

num=int(input("enter number 4: "))
s.add(num)

num=int(input("enter number 5: "))
s.add(num)

num=int(input("enter number 6: "))
s.add(num)

num=int(input("enter number 7: "))
s.add(num)

num=int(input("enter number 8: "))
s.add(num)

print(s)