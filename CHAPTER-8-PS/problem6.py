#  Write a python function which converts inches to cms.

# formulla => for converts in to cm   ~~ c.m = in × 2.54 
#           converts cm  to in   in = c.m / 2.54

def convert(i):
    return(i*2.54)

i=int(input("enter the number: "))
print(convert(i))