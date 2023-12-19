# practice  print code asci input
# print(ord('a'))
name = input('enter your name to acki code : ')
nameList = list(name)
print(nameList)
asciList = []
for  i in nameList :
     asciList.append(ord(i))
    
print(asciList)

dictName = {}


for j in nameList:
     dictName[j] = asciList[nameList.index(j)]

print(dictName) 
print(dictName.values()) 
print(str(asciList))


# m = 'mlkd'
# print(m.index("k"))  