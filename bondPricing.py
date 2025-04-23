import numpy as np

c = 50 #coupon payment
r = 0.04 #interest rate
n = 5 #years to maturity
f = 1000 #face value of the bond

total = 0
for i in range(1, n+1):
    cashflow = (c / (1 + r) ** i)
    print(cashflow)
    total += cashflow
total += (f / (1 + r) ** n)

print("total " + str(total))