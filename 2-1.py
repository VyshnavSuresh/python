a=[1,-2,34,-3,4,-22,6,-5]
print("Positive integer")
c=[x for x in a if x>0]
d=[x**2 for x in a ]
v=['a','e','i','o','u']
k=input("enter the string")
st=[x for x in k if x in v]
j=[ord(x) for x in k]

print("a - positive integers \n"+str(c))
print("\n b - squares \n"+str(d))
print("\n c - vowels \n"+str(st))
print("\n d - ordinal value \n"+str(j))

