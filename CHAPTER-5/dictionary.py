d={} # empty dictionary

marks={
    "raghav":54,
    "rajan":58,
    "aman":55
}


# print(marks,type(marks))

# print(marks["rajan"])
a= {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
# print(a["key"]) 
# print(a["list"]) 

# print(a.items())
# print(a.keys())
# print(a.values())
a.update({"marks":55,"id":102})
# print(a)
print(a.get("marks1")) # print none
print(a["marks1"])      # return as error