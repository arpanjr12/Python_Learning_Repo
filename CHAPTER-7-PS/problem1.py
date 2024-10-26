# Write a program to print multiplication table of a given number using for loop

num=int(input("enter your number: "))

for i in range(1,11):
    print(f"{num}X{i}={num*i}")