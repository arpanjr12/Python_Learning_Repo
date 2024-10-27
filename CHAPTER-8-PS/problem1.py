# . Write a program using functions to find greatest of three numbers.

def greatest(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num3 and num2>num1):
        return num2
    else:
        return num3
    
num1=int(input("enter the 1st number: "))
num2=int(input("enter the 2nd number: "))
num3=int(input("enter the 3rd number: "))

print (greatest(num1,num2,num3))

