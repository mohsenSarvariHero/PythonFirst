x = 7
y = 5
z = 8

print(x < 8 and y < 10 )
print(x < 8  &  y < 10 )
print(x  &  y  )
# & and 
# |  or
# ^  xor
# >> right shift
# << left shift

g = 24
print(g >> 1) # g // 2 ** 1
print(g >> 2) # g // 2 ** 2
print(g >> 3) # g // 2 ** 3

k = 12 
print(k << 1 )# k * 2 ** 1
print(k << 2 )# k * 2 ** 2


# binary 0b ....

d = 0b1001
print(d)
h = 4 # show in 8 bit
print(bin(h))


# ~  not -- متمم 2 عدد میگیرد تا اولین یک خودش بقیه معکوس می کند و در آخر هم یک منفی پشت عدد می گذارد

mn = 3 # 00000011 -->  11111011 --> 4 تا اول حذف میکنیم  -->       
# 1011 

# or

# -mn-1 = -3-1 = -4 
print(~mn)

