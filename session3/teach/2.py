# #وزن براساس کیلوگرم دریافت و به گرم نمایش بدهد
# x = 5
# print(x * 1000 , "g")

# # مساحت مثلث 
# height = int(input("enter number : "))
# ghaedeh = int(input("enter number : "))

# print(height , "*" , ghaedeh , "=", height*ghaedeh / 2 )

# create calculator

# x = int(input("enter number : "))
# y = int(input("enter number : "))
# z =(input("enter math : "))

# if(z == '*'):
#     print(" product " , x * y)
# elif( z == "+"):
#     print("sum : " , x + y)
# elif( z == "/"):
#     print("div : " , x / y)
# elif( z == "-"):
#     print("mines : " , x - y)


# print("sum : " , x + y)
# print(" product " , x * y)
# print("mines : " , x - y)
# print("div : " , x / y)

# seperate number

x = input("enter number : ")

y = list(x)
print(list(x))

for i in y :
    print(i , end = "_")
print()
result = ''.join(y)
print(result)


f = int(x)
list1 = []
while f != 0 :
    newF = f//10
    list1.append(f % 10)
    f = newF
print(list1)
for i in range(len(list1)):
    print(list1.pop())