# Write a python program using function to convert Celsius to Fahrenheit.


#  rules=> c/5 = (f-32)/9
#             c= 5*((f-32)/9)
#             f=(9*c+160)/5



def convert(c):
    return (9*c+160)/5

c=int(input("enter the temprature: "))
print(f"the converted value of Celsius to Fahrenheitis is:  {convert(c)}")