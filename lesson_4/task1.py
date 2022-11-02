# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
# !!ВНИМАНИЕ
# !!! не использовать константу math.pi


from decimal import Decimal, getcontext
getcontext().prec=11

pi = sum(1/Decimal(16)**k *(Decimal(4)/(8*k+1) -Decimal(2)/(8*k+4) -Decimal(1)/(8*k+5) -Decimal(1)/(8*k+6)) for k in range(10))

print(pi, round((pi),3),round((pi),1), round((pi),5), )
pi = str(pi)
print(pi, pi[0:5], pi[0:3], pi[0:7])