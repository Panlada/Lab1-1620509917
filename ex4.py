from math import log


n=int(input("Enter : "))
gamma = 0.57721566490153286060651209008240243104215933593992
for i in range(1, n):
    o =gamma + log(n) + 0.5/n - 1./(12*n**2) + 1./(120*n**4)
print("Limit = %d Value = %d"%n%o)
n=n-1