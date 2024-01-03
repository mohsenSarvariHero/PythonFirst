from decimal import Decimal
import fractions
x = 0.6 + 0.3 # 0.89999999999
y = Decimal(0.6) + Decimal(0.3)
z = Decimal('0.6') + Decimal('0.3')
f = float(Decimal('0.6') + Decimal('0.3'))
print(x)
print(y)
print(z)
print(type(z))
print(f)
print(type(f))
print( f == 0.9)



s = 1.5
print(fractions.Fraction(s))


c = 0b10101
print(c)



v = 2e+3 # 2 * 10**3
print(v)

g = -246.25
print(abs(g))


p = 1 + 3j
print(type(p))
print(p.real)

t = 21.5123
print(round(t, 2))

tt = 21.5153
print(round(tt))
print(round(tt, 2))


oi = 1_000_000_000_0
ol = 1_000_000_000_0.01
print(oi)
print(ol)