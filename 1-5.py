from math import gcd
a = int(input("enter the a"))
b = int(input("enter the b"))
print('GCD of', a, 'and', b, 'is', str(gcd(b,a %  b)))
if a > b:
    smaller = b
else:
    smaller = a
for i in range(1, smaller+1):
    if((a % i == 0) and (b % i == 0)):
        hcf = i
print("The H.C.F. is", str(hcf))