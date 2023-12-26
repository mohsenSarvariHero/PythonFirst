# id use for address variable that save in memory
# del use for delete variable

a = 5
b = a # point to the one place
c = 5 

print("a is  "  ,a)
print("address a in memory : " , id(a))
print("b is : " , b)
print("address b is : " , id(b))
print("c is : " , c)
print("address c is : " , id(c))

print("a , b in the same location in memory : " , id(a) == id(b))