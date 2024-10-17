num=("mango",1,5,2,3,8,9,0,"apple","banana","sunday",True,False,"apple","apple")  # 'Tupple' is immutable so we cannot change anything in  the tupple after created ...

# print(type(num))

# print(num)

print(len(num)) # 'len' use for find the length 

a=(2,) # if we want to create a tuple with a single value then we use ',' after the value
# print(type(a))

no=num.count("apple")  # 'count' use for count the element ...
# print(no)

b=(num.index("sunday"))
print(b) # 'index' use for return the original value of the given index number 
# '(num.index(3))' here '3' is the index number and the original value is ' 
