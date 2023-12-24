# is different with ==
# use id to undrastand
# is when true that lacation in same 

a = 2
b = 2
print(a == b )
print(a is b )

# location list different also that same  with variable id  ; id different
l1 = [1 , 2 ]
l2 = [1 , 2 ]

print(id(l1))
print(id(l2))

print(l1 is l2)
print(l1 == l2)