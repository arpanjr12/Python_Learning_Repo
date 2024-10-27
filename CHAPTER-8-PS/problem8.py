# Write a python function to print multiplication table of a given number

def multiplication(n):
    for i in range(1,21):
        print(f"{n} X {i} = {n*i}")

n=int(input("enter the number: "))
print( multiplication(n))