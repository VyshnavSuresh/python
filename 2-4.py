n=int(input("enter the no of elements in list1"))
m=int(input("enter the no of elments in list2"))
a=[]
b=[]
print("Enter list 1 elements")
for i in range(0,n+1):
    a.append(int(input("enter element")))
print("Enter list 2 elements")
for i in range(0,m+1):
    b.append(int(input("enter element")))
if len(a)==len(b):
    print("a-Length are same\n")
else:
    print("a-lenth are not same")
if sum(a) == sum(b):
    print("b-sum are equal")
else:
    print("b-sum are not equal")
j=[x for x in a if x in b]
if j != 0:
    print("c-same elements are",str(j))
else:
    print("c-no elements found")
